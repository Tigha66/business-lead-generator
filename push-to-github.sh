#!/bin/bash
# 🦞 Push to GitHub Script
# Run this after creating your GitHub repo

echo "🦞 Business Lead Generator - GitHub Push"
echo "========================================"
echo ""

# Check if remote exists
if git remote | grep -q '^origin$'; then
    echo "✅ Remote 'origin' already configured"
    git remote -v
else
    echo "❌ No remote configured"
    echo ""
    echo "Run these commands (replace YOUR_USERNAME):"
    echo ""
    echo "  git remote add origin https://github.com/YOUR_USERNAME/business-lead-generator.git"
    echo "  git push -u origin main"
    echo ""
    exit 1
fi

echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "📌 Next steps:"
    echo "   1. Create a release: git tag -a v1.0.0 -m 'Initial release'"
    echo "   2. Push tag: git push origin v1.0.0"
    echo "   3. Add repo description on GitHub"
    echo "   4. Share your repo!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Check your credentials and remote URL."
    echo ""
    echo "Troubleshooting:"
    echo "   - Make sure you created the repo on GitHub first"
    echo "   - Check remote URL: git remote -v"
    echo "   - Try: git remote set-url origin https://github.com/YOUR_USERNAME/business-lead-generator.git"
    echo ""
fi
