// LinkedIn Feed Component
class LinkedInFeed {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.options = {
            postsToShow: options.postsToShow || 6,
            dataSource: options.dataSource || '/components/linkedin-feed/data/posts.json',
            autoRefresh: options.autoRefresh || false,
            refreshInterval: options.refreshInterval || 300000, // 5 minutes
            showEngagement: options.showEngagement !== false,
            ...options
        };
        this.posts = [];
        this.init();
    }

    async init() {
        if (!this.container) {
            console.error('LinkedIn Feed: Container not found');
            return;
        }
        
        this.showLoading();
        await this.fetchPosts();
        
        if (this.options.autoRefresh) {
            setInterval(() => this.fetchPosts(), this.options.refreshInterval);
        }
    }

    showLoading() {
        this.container.innerHTML = `
            <div class="loading-spinner">
                <div style="font-size: 24px; margin-bottom: 10px;">⏳</div>
                <p>Loading LinkedIn posts...</p>
            </div>
        `;
    }

    showError(message) {
        this.container.innerHTML = `
            <div class="error-message">
                <div style="font-size: 24px; margin-bottom: 10px;">⚠️</div>
                <p>${message}</p>
            </div>
        `;
    }

    async fetchPosts() {
        try {
            const response = await fetch(this.options.dataSource);
            
            if (!response.ok) {
                throw new Error('Failed to fetch posts');
            }
            
            const data = await response.json();
            this.posts = data.posts || [];
            this.render();
        } catch (error) {
            console.error('LinkedIn Feed Error:', error);
            this.showError('Unable to load LinkedIn posts. Please try again later.');
        }
    }

    formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffTime = Math.abs(now - date);
        const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
        
        if (diffDays === 0) return 'Today';
        if (diffDays === 1) return 'Yesterday';
        if (diffDays < 7) return `${diffDays} days ago`;
        if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
        
        return date.toLocaleDateString('en-US', { 
            month: 'short', 
            day: 'numeric', 
            year: 'numeric' 
        });
    }

    formatNumber(num) {
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }

    createPostCard(post) {
        const engagementHTML = this.options.showEngagement ? `
            <div class="post-engagement">
                <div class="engagement-item">
                    <span class="engagement-icon">👍</span>
                    <span>${this.formatNumber(post.likes || 0)}</span>
                </div>
                <div class="engagement-item">
                    <span class="engagement-icon">💬</span>
                    <span>${this.formatNumber(post.comments || 0)}</span>
                </div>
            </div>
        ` : '';

        const imageHTML = post.image ? `
            <img src="${post.image}" alt="${post.title}" class="post-image" loading="lazy">
        ` : '';

        return `
            <article class="linkedin-post-card" onclick="window.open('${post.url}', '_blank')">
                <div class="post-header">
                    <div class="post-date">
                        📅 ${this.formatDate(post.date)}
                    </div>
                    <span class="post-badge">New</span>
                </div>
                <h3 class="post-title">${post.title}</h3>
                <p class="post-excerpt">${post.excerpt}</p>
                ${imageHTML}
                ${engagementHTML}
            </article>
        `;
    }

    render() {
        if (this.posts.length === 0) {
            this.showError('No posts available at the moment.');
            return;
        }

        const postsToDisplay = this.posts.slice(0, this.options.postsToShow);
        const postsHTML = postsToDisplay.map(post => this.createPostCard(post)).join('');

        this.container.innerHTML = `
            <div class="linkedin-posts-grid">
                ${postsHTML}
            </div>
            <div class="linkedin-view-more">
                <a href="https://www.linkedin.com/company/27br/" 
                   target="_blank" 
                   rel="noopener noreferrer" 
                   class="view-more-btn">
                    View All Posts on LinkedIn
                    <span>→</span>
                </a>
            </div>
        `;
    }

    // Public method to manually refresh posts
    refresh() {
        this.fetchPosts();
    }

    // Public method to update options
    updateOptions(newOptions) {
        this.options = { ...this.options, ...newOptions };
        this.render();
    }
}

// Alternative: Fetch from LinkedIn RSS (if available)
class LinkedInRSSFeed extends LinkedInFeed {
    async fetchPosts() {
        try {
            // Using RSS2JSON service (free tier available)
            const rssUrl = this.options.rssUrl || 'https://www.linkedin.com/company/27br/';
            const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(rssUrl)}`;
            
            const response = await fetch(apiUrl);
            
            if (!response.ok) {
                throw new Error('Failed to fetch RSS feed');
            }
            
            const data = await response.json();
            
            // Transform RSS data to our post format
            this.posts = data.items.map((item, index) => ({
                id: index + 1,
                title: item.title,
                excerpt: this.stripHtml(item.description).substring(0, 150) + '...',
                date: item.pubDate.split(' ')[0],
                url: item.link,
                image: this.extractImage(item.description),
                likes: 0,
                comments: 0
            }));
            
            this.render();
        } catch (error) {
            console.error('LinkedIn RSS Feed Error:', error);
            this.showError('Unable to load LinkedIn posts. Please try again later.');
        }
    }

    stripHtml(html) {
        const tmp = document.createElement('div');
        tmp.innerHTML = html;
        return tmp.textContent || tmp.innerText || '';
    }

    extractImage(html) {
        const imgRegex = /<img[^>]+src="([^">]+)"/;
        const match = html.match(imgRegex);
        return match ? match[1] : null;
    }
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { LinkedInFeed, LinkedInRSSFeed };
}

