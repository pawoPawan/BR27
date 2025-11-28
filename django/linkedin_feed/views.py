"""
LinkedIn Feed Views
Fetches and serves LinkedIn posts from BR27's company page
"""
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
import requests
from datetime import datetime
import re


def extract_image_from_description(description):
    """Extract first image URL from HTML description"""
    if not description:
        return None
    img_match = re.search(r'<img[^>]+src="([^">]+)"', description)
    return img_match.group(1) if img_match else None


def strip_html(html):
    """Remove HTML tags from text"""
    if not html:
        return ""
    return re.sub('<[^<]+?>', '', html)


@require_http_methods(["GET"])
@cache_page(60 * 15)  # Cache for 15 minutes
def fetch_linkedin_posts(request):
    """
    Fetch LinkedIn posts from BR27's company page using RSS2JSON service
    
    Endpoint: /api/linkedin/posts/
    
    Query params:
    - count: Number of posts to return (default: 10, max: 20)
    """
    try:
        # Get number of posts to return
        count = min(int(request.GET.get('count', 10)), 20)
        
        # BR27 LinkedIn company page RSS feed
        # Note: LinkedIn RSS feeds are sometimes available via RSS2JSON or similar services
        linkedin_rss_url = "https://www.linkedin.com/company/27br/posts/"
        
        # Option 1: Try RSS2JSON service (free tier available)
        rss2json_url = f"https://api.rss2json.com/v1/api.json?rss_url={linkedin_rss_url}&count={count}"
        
        # Make request to RSS2JSON
        response = requests.get(rss2json_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if we got valid data
            if data.get('status') == 'ok' and 'items' in data:
                posts = []
                
                for idx, item in enumerate(data['items'][:count], 1):
                    # Parse the post data
                    post = {
                        'id': idx,
                        'title': item.get('title', 'LinkedIn Post'),
                        'excerpt': strip_html(item.get('description', ''))[:200] + '...',
                        'description': strip_html(item.get('description', '')),
                        'date': item.get('pubDate', '').split(' ')[0] if item.get('pubDate') else datetime.now().strftime('%Y-%m-%d'),
                        'url': item.get('link', 'https://www.linkedin.com/company/27br/'),
                        'image': extract_image_from_description(item.get('description')),
                        'author': item.get('author', 'BR27'),
                        'categories': item.get('categories', [])
                    }
                    posts.append(post)
                
                return JsonResponse({
                    'success': True,
                    'count': len(posts),
                    'posts': posts,
                    'lastUpdated': datetime.now().isoformat(),
                    'source': 'linkedin-rss'
                })
            else:
                # If RSS2JSON fails, return fallback data
                return get_fallback_data(count)
        else:
            return get_fallback_data(count)
            
    except requests.Timeout:
        return JsonResponse({
            'success': False,
            'error': 'Request timeout',
            'message': 'LinkedIn feed took too long to respond'
        }, status=504)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'message': 'Error fetching LinkedIn posts'
        }, status=500)


def get_fallback_data(count=10):
    """
    Return fallback data when LinkedIn API is unavailable
    This uses the static JSON file as backup
    """
    import json
    import os
    from django.conf import settings
    
    try:
        # Try to load from static data file
        data_file = os.path.join(settings.BASE_DIR, '..', 'components', 'linkedin-feed', 'data', 'posts.json')
        
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                posts = data.get('posts', [])[:count]
                
                return JsonResponse({
                    'success': True,
                    'count': len(posts),
                    'posts': posts,
                    'lastUpdated': data.get('lastUpdated', datetime.now().strftime('%Y-%m-%d')),
                    'source': 'fallback',
                    'message': 'Using cached data - LinkedIn API unavailable'
                })
    except Exception as e:
        pass
    
    # Ultimate fallback: hardcoded sample data
    sample_posts = [
        {
            'id': 1,
            'title': 'Empowering Rural Communities Through Technology',
            'excerpt': 'Discover how digital literacy programs are transforming villages across India...',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'url': 'https://www.linkedin.com/company/27br/',
            'image': None,
            'likes': 0,
            'comments': 0
        },
        {
            'id': 2,
            'title': 'Career Guidance: Making Informed Decisions',
            'excerpt': 'Science, Commerce, or Arts? Here\'s our comprehensive guide...',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'url': 'https://www.linkedin.com/company/27br/',
            'image': None,
            'likes': 0,
            'comments': 0
        },
        {
            'id': 3,
            'title': 'Financial Literacy Workshop Success',
            'excerpt': 'Our recent workshop reached 200+ young professionals...',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'url': 'https://www.linkedin.com/company/27br/',
            'image': None,
            'likes': 0,
            'comments': 0
        }
    ]
    
    return JsonResponse({
        'success': True,
        'count': len(sample_posts[:count]),
        'posts': sample_posts[:count],
        'lastUpdated': datetime.now().isoformat(),
        'source': 'sample',
        'message': 'Using sample data - LinkedIn feed unavailable'
    })


@require_http_methods(["GET"])
def linkedin_feed_status(request):
    """
    Check LinkedIn feed connection status
    Endpoint: /api/linkedin/status/
    """
    try:
        rss2json_url = "https://api.rss2json.com/v1/api.json?rss_url=https://www.linkedin.com/company/27br/posts/&count=1"
        response = requests.get(rss2json_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'ok':
                return JsonResponse({
                    'status': 'connected',
                    'service': 'rss2json',
                    'message': 'LinkedIn feed is accessible'
                })
        
        return JsonResponse({
            'status': 'unavailable',
            'message': 'LinkedIn feed is currently unavailable',
            'fallback': 'Using cached data'
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

