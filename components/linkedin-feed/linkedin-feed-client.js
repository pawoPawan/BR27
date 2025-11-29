// Client-Side LinkedIn Feed - Works on GitHub Pages
// Fetches LinkedIn posts directly in browser using RSS2JSON API

class LinkedInFeedClient {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.options = {
            postsToShow: options.postsToShow || 3,
            companyUrl: options.companyUrl || 'https://www.linkedin.com/company/27br/',
            carousel: options.carousel !== false,
            carouselInterval: options.carouselInterval || 5000,
            autoRefresh: options.autoRefresh || false,
            refreshInterval: options.refreshInterval || 300000, // 5 minutes
            showEngagement: options.showEngagement !== false,
            fallbackData: options.fallbackData || '/components/linkedin-feed/data/posts.json',
            ...options
        };
        this.posts = [];
        this.currentSlide = 0;
        this.carouselTimer = null;
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

        if (this.options.carousel && this.posts.length > 1) {
            this.startCarousel();
        }
    }

    showLoading() {
        this.container.innerHTML = `
            <div class="loading-spinner">
                <div class="spinner-icon">⏳</div>
                <p>Fetching latest LinkedIn posts...</p>
            </div>
        `;
    }

    showError(message) {
        this.container.innerHTML = `
            <div class="error-message">
                <div class="error-icon">⚠️</div>
                <p>${message}</p>
            </div>
        `;
    }

    async fetchPosts() {
        try {
            // Try fetching from LinkedIn via RSS2JSON
            const rssUrl = `${this.options.companyUrl}posts/`;
            const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(rssUrl)}&count=${this.options.postsToShow}`;
            
            console.log('Fetching from LinkedIn RSS...');
            
            const response = await fetch(apiUrl);
            const data = await response.json();
            
            if (data.status === 'ok' && data.items && data.items.length > 0) {
                // Successfully fetched from LinkedIn
                this.posts = this.transformRSSData(data.items);
                console.log('✅ Loaded from LinkedIn RSS:', this.posts.length, 'posts');
                this.render();
            } else {
                throw new Error('RSS feed unavailable or empty');
            }
        } catch (error) {
            console.warn('LinkedIn RSS not available, using fallback data:', error.message);
            // Fallback to static JSON
            await this.loadFallbackData();
        }
    }

    async loadFallbackData() {
        try {
            const response = await fetch(this.options.fallbackData);
            const data = await response.json();
            this.posts = data.posts.slice(0, this.options.postsToShow);
            console.log('✅ Loaded from fallback data:', this.posts.length, 'posts');
            this.render();
        } catch (error) {
            console.error('Failed to load fallback data:', error);
            this.showError('Unable to load LinkedIn posts. Please try again later.');
        }
    }

    transformRSSData(items) {
        return items.map((item, index) => ({
            id: index + 1,
            title: item.title || 'LinkedIn Post',
            excerpt: this.stripHtml(item.description || '').substring(0, 200) + '...',
            description: this.stripHtml(item.description || ''),
            date: this.parseDate(item.pubDate),
            url: item.link || this.options.companyUrl,
            image: this.extractImage(item.description),
            author: item.author || 'BR27',
            likes: 0, // RSS doesn't provide engagement data
            comments: 0
        }));
    }

    stripHtml(html) {
        const tmp = document.createElement('div');
        tmp.innerHTML = html;
        return tmp.textContent || tmp.innerText || '';
    }

    extractImage(html) {
        if (!html) return null;
        const imgMatch = html.match(/<img[^>]+src="([^">]+)"/);
        return imgMatch ? imgMatch[1] : null;
    }

    parseDate(dateString) {
        if (!dateString) return new Date().toISOString().split('T')[0];
        const date = new Date(dateString);
        return date.toISOString().split('T')[0];
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
        if (!num) return '0';
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }

    createPostCard(post, index) {
        const engagementHTML = this.options.showEngagement && (post.likes || post.comments) ? `
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
            <article class="linkedin-post-card ${this.options.carousel ? 'carousel-slide' : ''}" 
                     data-slide="${index}"
                     onclick="window.open('${post.url}', '_blank')">
                <div class="post-header">
                    <div class="post-date">
                        📅 ${this.formatDate(post.date)}
                    </div>
                    <span class="post-badge">LinkedIn</span>
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

        const postsHTML = this.posts.map((post, index) => this.createPostCard(post, index)).join('');

        if (this.options.carousel) {
            this.container.innerHTML = `
                <div class="linkedin-carousel">
                    <div class="carousel-container">
                        ${postsHTML}
                    </div>
                    ${this.posts.length > 1 ? `
                        <button class="carousel-btn prev-btn" aria-label="Previous">‹</button>
                        <button class="carousel-btn next-btn" aria-label="Next">›</button>
                        <div class="carousel-dots">
                            ${this.posts.map((_, i) => `<span class="dot ${i === 0 ? 'active' : ''}" data-slide="${i}"></span>`).join('')}
                        </div>
                    ` : ''}
                </div>
                <div class="linkedin-view-more">
                    <a href="/linkedin-articles.html" class="view-more-btn">
                        View All Articles
                        <span>→</span>
                    </a>
                </div>
            `;

            if (this.posts.length > 1) {
                this.attachCarouselEvents();
                // Show first slide
                setTimeout(() => this.updateCarousel(), 100);
            }
        } else {
            this.container.innerHTML = `
                <div class="linkedin-posts-grid">
                    ${postsHTML}
                </div>
                <div class="linkedin-view-more">
                    <a href="/linkedin-articles.html" class="view-more-btn">
                        View All Articles
                        <span>→</span>
                    </a>
                </div>
            `;
        }
    }

    attachCarouselEvents() {
        const prevBtn = this.container.querySelector('.prev-btn');
        const nextBtn = this.container.querySelector('.next-btn');
        const dots = this.container.querySelectorAll('.dot');

        if (prevBtn) prevBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.prevSlide();
        });
        
        if (nextBtn) nextBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.nextSlide();
        });

        dots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                e.stopPropagation();
                this.goToSlide(parseInt(dot.dataset.slide));
            });
        });
    }

    startCarousel() {
        this.carouselTimer = setInterval(() => {
            this.nextSlide();
        }, this.options.carouselInterval);

        // Pause on hover
        const carousel = this.container.querySelector('.linkedin-carousel');
        if (carousel) {
            carousel.addEventListener('mouseenter', () => this.pauseCarousel());
            carousel.addEventListener('mouseleave', () => this.startCarousel());
        }
    }

    pauseCarousel() {
        if (this.carouselTimer) {
            clearInterval(this.carouselTimer);
            this.carouselTimer = null;
        }
    }

    nextSlide() {
        this.currentSlide = (this.currentSlide + 1) % this.posts.length;
        this.updateCarousel();
    }

    prevSlide() {
        this.currentSlide = (this.currentSlide - 1 + this.posts.length) % this.posts.length;
        this.updateCarousel();
    }

    goToSlide(index) {
        this.currentSlide = index;
        this.updateCarousel();
    }

    updateCarousel() {
        const slides = this.container.querySelectorAll('.carousel-slide');
        const dots = this.container.querySelectorAll('.dot');

        slides.forEach((slide, index) => {
            slide.classList.toggle('active', index === this.currentSlide);
        });

        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === this.currentSlide);
        });
    }

    refresh() {
        this.fetchPosts();
    }

    updateOptions(newOptions) {
        this.options = { ...this.options, ...newOptions };
        if (newOptions.carousel === false && this.carouselTimer) {
            this.pauseCarousel();
        }
        this.render();
    }

    destroy() {
        this.pauseCarousel();
        if (this.container) {
            this.container.innerHTML = '';
        }
    }
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LinkedInFeedClient;
}

