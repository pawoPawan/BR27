#!/usr/bin/env python3
"""
Platform Migration Helper for BR27 Website

Helps migrate between GitHub Pages (Jekyll) and Django

Usage:
    python scripts/migrate-platform.py --to django
    python scripts/migrate-platform.py --to github
    python scripts/migrate-platform.py --status
"""

import json
import os
import sys
import shutil
from pathlib import Path

class PlatformMigrator:
    def __init__(self, project_root='.'):
        self.root = Path(project_root)
        self.platform_config = self.root / 'config' / 'platform.json'
        
    def get_current_platform(self):
        """Get current platform from config"""
        with open(self.platform_config, 'r') as f:
            config = json.load(f)
            return config['platform']['current']
    
    def set_platform(self, platform):
        """Set platform in config"""
        with open(self.platform_config, 'r') as f:
            config = json.load(f)
        
        config['platform']['current'] = platform
        
        # Update features based on platform
        if platform == 'django':
            config['features']['api_enabled'] = True
            config['features']['use_static_fallback'] = True
        else:
            config['features']['api_enabled'] = False
            config['features']['use_static_fallback'] = True
        
        with open(self.platform_config, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Platform set to: {platform}")
    
    def sync_templates(self, direction):
        """Sync templates between Jekyll and Django"""
        if direction == 'to_django':
            src = self.root / '_includes'
            dst = self.root / 'django' / 'templates' / 'components'
            
            print("📋 Syncing templates: Jekyll → Django")
            
            # Convert Liquid syntax to Jinja2
            for file in src.glob('*.html'):
                content = file.read_text()
                
                # Basic conversions
                content = content.replace('{% comment %}', '{# ')
                content = content.replace('{% endcomment %}', ' #}')
                content = content.replace('| default:', '|default:')
                
                dst_file = dst / file.name
                dst_file.write_text(content)
                print(f"  ✅ {file.name}")
        
        elif direction == 'to_jekyll':
            src = self.root / 'django' / 'templates' / 'components'
            dst = self.root / '_includes'
            
            print("📋 Syncing templates: Django → Jekyll")
            
            for file in src.glob('*.html'):
                content = file.read_text()
                
                # Basic conversions
                content = content.replace('{# ', '{% comment %}')
                content = content.replace(' #}', '{% endcomment %}')
                content = content.replace('|default:', '| default:')
                
                dst_file = dst / file.name
                dst_file.write_text(content)
                print(f"  ✅ {file.name}")
    
    def show_status(self):
        """Show current platform status"""
        current = self.get_current_platform()
        
        with open(self.platform_config, 'r') as f:
            config = json.load(f)
        
        print("\n" + "="*50)
        print("BR27 Platform Status")
        print("="*50 + "\n")
        
        print(f"Current Platform: {current.upper()}")
        print(f"API Enabled: {config['features']['api_enabled']}")
        print(f"Static Fallback: {config['features']['use_static_fallback']}")
        
        routing = config['routing'][current]
        print(f"\nCurrent Routing:")
        print(f"  Base URL: {routing['base_url']}")
        print(f"  Static Path: {routing['static_path']}")
        print(f"  API Path: {routing['api_path']}")
        print(f"  Template Engine: {routing['template_engine']}")
        
        print("\n" + "="*50)
    
    def migrate_to_django(self):
        """Full migration to Django"""
        print("\n🚀 Migrating to Django Platform\n")
        
        # Step 1: Set platform
        self.set_platform('django')
        
        # Step 2: Sync templates
        self.sync_templates('to_django')
        
        # Step 3: Instructions
        print("\n📋 Next Steps:\n")
        print("1. Deploy Django backend to hosting service")
        print("2. Run: cd django && python manage.py collectstatic")
        print("3. Configure your hosting environment variables")
        print("4. Update DNS to point to new server")
        print("5. Test feeds are working with API")
        
        print("\n✅ Configuration updated for Django!")
        print("📝 See MIGRATION_GUIDE.md for detailed instructions")
    
    def migrate_to_github(self):
        """Revert to GitHub Pages"""
        print("\n🔙 Reverting to GitHub Pages\n")
        
        # Step 1: Set platform
        self.set_platform('github')
        
        # Step 2: Sync templates
        self.sync_templates('to_jekyll')
        
        print("\n✅ Configuration updated for GitHub Pages!")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/migrate-platform.py --to django")
        print("  python scripts/migrate-platform.py --to github")
        print("  python scripts/migrate-platform.py --status")
        sys.exit(1)
    
    migrator = PlatformMigrator()
    
    command = sys.argv[1]
    
    if command == '--status':
        migrator.show_status()
    elif command == '--to' and len(sys.argv) > 2:
        target = sys.argv[2]
        if target == 'django':
            migrator.migrate_to_django()
        elif target == 'github':
            migrator.migrate_to_github()
        else:
            print(f"❌ Unknown platform: {target}")
            sys.exit(1)
    else:
        print("❌ Invalid command")
        sys.exit(1)

if __name__ == '__main__':
    main()

