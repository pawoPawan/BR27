#!/usr/bin/env python3
"""
LinkedIn Posts Updater for BR27 Website

This script helps you manually update LinkedIn posts or can be automated.
Usage: cd components/linkedin-feed/scripts && python3 update-posts.py
"""

import json
from datetime import datetime
from typing import List, Dict

def get_post_from_user() -> Dict:
    """Interactive CLI to get post details from user"""
    print("\n" + "="*50)
    print("Add New LinkedIn Post to BR27 Website")
    print("="*50 + "\n")
    
    post = {
        "id": int(input("Post ID (number): ")),
        "title": input("Post Title: "),
        "excerpt": input("Brief Description (1-2 sentences): "),
        "date": input("Date (YYYY-MM-DD) or press Enter for today: ") or datetime.now().strftime("%Y-%m-%d"),
        "url": input("LinkedIn Post URL: "),
        "image": input("Image URL (optional, press Enter to skip): ") or None,
        "likes": int(input("Number of Likes: ") or "0"),
        "comments": int(input("Number of Comments: ") or "0")
    }
    
    return post

def load_posts() -> Dict:
    """Load existing posts from JSON file"""
    try:
        with open('../data/posts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"posts": [], "lastUpdated": ""}

def save_posts(data: Dict) -> None:
    """Save posts to JSON file"""
    data["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")
    with open('../data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Successfully saved to data/posts.json")
    print(f"📅 Last updated: {data['lastUpdated']}")

def display_posts(posts: List[Dict]) -> None:
    """Display current posts"""
    if not posts:
        print("No posts found.")
        return
    
    print("\n" + "="*50)
    print("Current LinkedIn Posts")
    print("="*50 + "\n")
    
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']}")
        print(f"   Date: {post['date']}")
        print(f"   Engagement: {post['likes']} likes, {post['comments']} comments")
        print(f"   URL: {post['url']}\n")

def main():
    """Main function"""
    print("""
    ╔══════════════════════════════════════════════╗
    ║  BR27 LinkedIn Posts Manager                 ║
    ║  Update your website's LinkedIn feed         ║
    ╚══════════════════════════════════════════════╝
    """)
    
    data = load_posts()
    
    while True:
        print("\nOptions:")
        print("1. View current posts")
        print("2. Add new post")
        print("3. Remove a post")
        print("4. Update engagement stats")
        print("5. Save and exit")
        print("6. Exit without saving")
        
        choice = input("\nYour choice (1-6): ").strip()
        
        if choice == "1":
            display_posts(data["posts"])
        
        elif choice == "2":
            new_post = get_post_from_user()
            data["posts"].insert(0, new_post)  # Add to beginning
            print("\n✅ Post added!")
            display_posts(data["posts"])
        
        elif choice == "3":
            display_posts(data["posts"])
            try:
                index = int(input("\nEnter post number to remove: ")) - 1
                removed = data["posts"].pop(index)
                print(f"\n✅ Removed: {removed['title']}")
            except (ValueError, IndexError):
                print("❌ Invalid post number")
        
        elif choice == "4":
            display_posts(data["posts"])
            try:
                index = int(input("\nEnter post number to update: ")) - 1
                post = data["posts"][index]
                print(f"\nUpdating: {post['title']}")
                post["likes"] = int(input(f"New likes count (current: {post['likes']}): ") or post["likes"])
                post["comments"] = int(input(f"New comments count (current: {post['comments']}): ") or post["comments"])
                print("✅ Engagement updated!")
            except (ValueError, IndexError):
                print("❌ Invalid post number")
        
        elif choice == "5":
            save_posts(data)
            print("\n👋 Goodbye!")
            break
        
        elif choice == "6":
            print("\n👋 Exiting without saving...")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

def quick_add_sample_posts():
    """Quick function to add sample posts for testing"""
    sample_posts = {
        "posts": [
            {
                "id": 1,
                "title": "Empowering Rural Communities Through Technology",
                "excerpt": "Discover how digital literacy programs are transforming villages across India. Our latest initiative brings internet connectivity and tech training to 50+ rural communities.",
                "date": "2025-11-25",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 156,
                "comments": 23
            },
            {
                "id": 2,
                "title": "Career Guidance: Choosing the Right Stream After 10th",
                "excerpt": "Science, Commerce, or Arts? Here's our comprehensive guide to help students make informed decisions based on their interests, not societal pressure.",
                "date": "2025-11-22",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 203,
                "comments": 45
            },
            {
                "id": 3,
                "title": "Financial Literacy Workshop - 200+ Participants",
                "excerpt": "Our recent workshop on smart investing and savings strategies reached 200+ young professionals. Building financial awareness one session at a time.",
                "date": "2025-11-18",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 178,
                "comments": 31
            },
            {
                "id": 4,
                "title": "Understanding Governance: Your Rights & Responsibilities",
                "excerpt": "Transparency in policy-making starts with informed citizens. Our latest blog breaks down complex government policies into actionable insights.",
                "date": "2025-11-15",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 142,
                "comments": 18
            },
            {
                "id": 5,
                "title": "Skills That Matter: Future-Proofing Your Career",
                "excerpt": "In a rapidly changing job market, these 10 skills will keep you relevant. Our comprehensive guide to continuous learning and professional development.",
                "date": "2025-11-12",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 267,
                "comments": 52
            },
            {
                "id": 6,
                "title": "BR27 Community Milestone: 10,000 Lives Impacted",
                "excerpt": "Celebrating our journey of empowering minds across India. Thank you to our community for making this possible. This is just the beginning!",
                "date": "2025-11-08",
                "url": "https://www.linkedin.com/company/27br/",
                "image": None,
                "likes": 523,
                "comments": 89
            }
        ],
        "lastUpdated": datetime.now().strftime("%Y-%m-%d")
    }
    
    with open('../data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(sample_posts, f, indent=2, ensure_ascii=False)
    
    print("✅ Sample posts added to data/posts.json")
    print("📊 Added 6 sample posts with realistic engagement numbers")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        quick_add_sample_posts()
    else:
        main()

