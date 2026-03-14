#!/bin/bash
# 🦞 Quick Push to GitHub
# Run this script to push to your GitHub repo

echo "🦞 Pushing to GitHub..."
echo ""

# Check if gh CLI is available
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI found"
    echo "Running: gh auth login"
    gh auth login
    
    echo ""
    echo "Now pushing..."
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ SUCCESS! Your repo is live at:"
        echo "https://github.com/Tigha66/business-lead-generator"
        echo ""
        echo "🎉 Next steps:"
        echo "   1. Add repo description on GitHub"
        echo "   2. Create release: git tag -a v1.0.0 -m 'v1.0.0'"
        echo "   3. git push origin v1.0.0"
        echo "   4. Share your repo!"
    else
        echo "❌ Push failed"
    fi
else
    echo "❌ GitHub CLI (gh) not found"
    echo ""
    echo "Install it:"
    echo "  brew install gh           # macOS"
    echo "  sudo apt install gh       # Linux"
    echo "  winget install GitHub.cli # Windows"
    echo ""
    echo "OR use a Personal Access Token:"
    echo "  1. Go to: https://github.com/settings/tokens"
    echo "  2. Create token with 'repo' scope"
    echo "  3. Run: git remote set-url origin https://YOUR_TOKEN@github.com/Tigha66/business-lead-generator.git"
    echo "  4. Run: git push -u origin main"
fi
