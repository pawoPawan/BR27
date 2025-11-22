#!/bin/bash

# BR27 GitHub Deployment Script
# Automates the process of pushing to GitHub

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Check if git is initialized
if [ ! -d ".git" ]; then
    print_error "Git repository not initialized"
    print_info "Initializing git repository..."
    git init
    print_success "Git initialized"
fi

# Check if remote exists
if ! git remote | grep -q origin; then
    print_warning "No remote repository configured"
    echo ""
    print_info "Please enter your GitHub repository URL:"
    echo "Example: https://github.com/pawoPawan/br27.git"
    read -p "Repository URL: " REPO_URL
    
    if [ -z "$REPO_URL" ]; then
        print_error "No URL provided. Exiting."
        exit 1
    fi
    
    git remote add origin "$REPO_URL"
    print_success "Remote added: $REPO_URL"
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)

if [ -z "$CURRENT_BRANCH" ]; then
    print_info "Creating main branch..."
    git checkout -b main
    CURRENT_BRANCH="main"
fi

print_info "Current branch: $CURRENT_BRANCH"

# Check for uncommitted changes
if [[ -n $(git status -s) ]]; then
    print_info "Changes detected. Staging files..."
    
    # Add all files
    git add .
    
    # Get commit message
    if [ -z "$1" ]; then
        read -p "Commit message (or press Enter for default): " COMMIT_MSG
        if [ -z "$COMMIT_MSG" ]; then
            COMMIT_MSG="Update BR27 website - $(date '+%Y-%m-%d %H:%M:%S')"
        fi
    else
        COMMIT_MSG="$1"
    fi
    
    # Commit changes
    git commit -m "$COMMIT_MSG"
    print_success "Changes committed: $COMMIT_MSG"
else
    print_warning "No changes to commit"
fi

# Push to GitHub
print_info "Pushing to GitHub..."

if git push origin "$CURRENT_BRANCH" 2>&1; then
    print_success "Successfully pushed to GitHub!"
    echo ""
    print_success "🚀 Your website is being deployed to GitHub Pages"
    print_info "It may take 1-5 minutes to go live"
    echo ""
    
    # Get repository URL
    REMOTE_URL=$(git remote get-url origin)
    REPO_NAME=$(basename "$REMOTE_URL" .git)
    GITHUB_USER=$(basename $(dirname "$REMOTE_URL"))
    
    if [[ "$REMOTE_URL" == *"github.com"* ]]; then
        print_info "GitHub Pages URL: https://${GITHUB_USER}.github.io/${REPO_NAME}/"
        
        # Check if CNAME exists
        if [ -f "CNAME" ]; then
            CUSTOM_DOMAIN=$(cat CNAME)
            print_info "Custom domain configured: https://${CUSTOM_DOMAIN}"
            echo ""
            print_warning "Don't forget to configure your DNS settings!"
            print_info "See DEPLOYMENT.md for detailed DNS configuration"
        fi
    fi
    
    echo ""
    print_info "View your repository: ${REMOTE_URL%.git}"
    
else
    print_error "Failed to push to GitHub"
    print_info "If this is your first push, try:"
    echo "  git push -u origin $CURRENT_BRANCH"
    exit 1
fi

echo ""
print_success "Deployment complete! 🎉"

