#!/bin/bash

# Student App Store - GitHub Deployment Script
# This script helps you deploy your app to GitHub and Render

echo "🚀 Student App Store - Deployment Setup"
echo "========================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Student App Store with Google OAuth"
    echo "✅ Git repository initialized"
else
    echo "📝 Git repository already exists"
fi

# Check if remote origin exists
if git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 GitHub remote already configured"
    echo "Current remote: $(git remote get-url origin)"
else
    echo "❓ Please provide your GitHub repository URL:"
    echo "Example: https://github.com/yourusername/student-app-store.git"
    read -p "GitHub URL: " github_url

    if [ ! -z "$github_url" ]; then
        git remote add origin "$github_url"
        echo "✅ GitHub remote added"
    else
        echo "⚠️  No GitHub URL provided. Please add it manually:"
        echo "git remote add origin https://github.com/yourusername/student-app-store.git"
    fi
fi

echo ""
echo "📤 Ready to push to GitHub?"
echo "Run these commands:"
echo "  git push -u origin main"
echo ""

echo "🌐 After pushing to GitHub, deploy to Render:"
echo "1. Go to https://dashboard.render.com"
echo "2. Click 'New' → 'Web Service'"
echo "3. Connect your GitHub repository"
echo "4. Configure with:"
echo "   - Runtime: Python 3"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: python app.py"
echo "5. Add environment variables in Render dashboard"
echo ""

echo "🔐 Don't forget to:"
echo "- Set up Google OAuth credentials in Google Cloud Console"
echo "- Add your Render domain to authorized redirect URIs"
echo "- Configure environment variables in Render"
echo ""

echo "🎉 Happy deploying!"