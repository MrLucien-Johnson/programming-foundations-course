# GitHub Setup Guide: Programming Foundations Course

This guide walks you through creating a GitHub repository and pushing your course content.

---

## ✅ Prerequisites

Before starting, ensure you have:

- [ ] Git installed on your computer
  - **Check:** Run `git --version` in terminal
  - **Install:** Download from https://git-scm.com/downloads
- [ ] A GitHub account
  - **Sign up:** https://github.com/signup (free)
- [ ] Your course files ready (they should be!)

---

## 🚀 PATH A: GitHub Website (Recommended - Safest)

### Step 1: Create Repository on GitHub

1. **Go to GitHub:** https://github.com/new
2. **Repository name:** `programming-foundations-course` (or your preferred name)
3. **Description:** "Beginner-friendly Python and C# programming course with portfolio projects"
4. **Visibility:** Select **Private** (for soft launch with 2 testers)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### Step 2: Initialize Git Locally (If Not Done)

Open terminal/PowerShell in your course directory and run:

```bash
# Navigate to your course directory
cd "D:\AbelSolutions\Apps\Courses\BeginnersC#"

# Initialize git repository
git init

# Set default branch to main
git config --local init.defaultBranch main

# Configure your name and email (if not already set globally)
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 3: Stage and Commit Files

```bash
# Stage all course content
git add python-beginner-workbook/
git add csharp-beginner-workbook/
git add Programming-Foundations-Course/
git add README.md START-HERE.md HOW-TO-USE.md COURSE-LINKS.md
git add TESTER-ACCESS.md GUMROAD-DELIVERY-GITHUB.md
git add STRUCTURE-NOTES.md

# Commit course content
git commit -m "Initial course content and structure"

# Stage repo hygiene files
git add .gitignore LICENSE .gitattributes PLACEHOLDERS-TO-FILL.md Notion-Hub/

# Commit repo setup files
git commit -m "Add repo hygiene files and placeholder report"
```

### Step 4: Connect to GitHub and Push

```bash
# Add GitHub repository as remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/programming-foundations-course.git

# Push to GitHub
git push -u origin main
```

**Note:** GitHub will prompt for authentication. Use:
- Personal Access Token (recommended), or
- GitHub CLI authentication

---

## ⚡ PATH B: GitHub CLI (Fastest - If Available)

### Step 1: Check if GitHub CLI is Installed

```bash
gh --version
```

If installed, proceed. If not, see "Installing GitHub CLI" below.

### Step 2: Authenticate with GitHub

```bash
gh auth login
```

Follow the prompts to authenticate.

### Step 3: Create Repository and Push in One Command

```bash
# Navigate to your course directory
cd "D:\AbelSolutions\Apps\Courses\BeginnersC#"

# Initialize git (if not done)
git init
git config --local init.defaultBranch main

# Stage and commit files (same as Path A, Step 3)
git add .
git commit -m "Initial course content and structure"

# Create private repo and push
gh repo create programming-foundations-course --private --source=. --remote=origin --push
```

**That's it!** The repository is created and your code is pushed.

---

## 📦 Installing GitHub CLI (Optional)

If you want to use GitHub CLI:

**Windows:**
```powershell
# Using winget
winget install --id GitHub.cli

# Or download from: https://cli.github.com/
```

**Mac:**
```bash
brew install gh
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install gh

# Fedora
sudo dnf install gh
```

After installation, authenticate:
```bash
gh auth login
```

---

## 👥 Inviting Testers (2 People)

### Method 1: Via GitHub Website

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Collaborators** (left sidebar)
4. Click **Add people**
5. Enter tester's GitHub username or email
6. Select permission: **Read** (testers only need read access)
7. Click **Add [username] to this repository**
8. Repeat for second tester

### Method 2: Via GitHub CLI

```bash
# Invite first tester
gh api repos/YOUR_USERNAME/programming-foundations-course/collaborators/TESTER_USERNAME -X PUT -f permission=push

# Invite second tester
gh api repos/YOUR_USERNAME/programming-foundations-course/collaborators/TESTER_USERNAME_2 -X PUT -f permission=push
```

**Note:** Replace `YOUR_USERNAME`, `TESTER_USERNAME`, etc. with actual usernames.

---

## 🏷️ Creating a Release Tag (v1.0-softlaunch)

### Via GitHub Website

1. Go to your repository
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. **Tag version:** `v1.0-softlaunch`
5. **Release title:** `v1.0 Soft Launch`
6. **Description:** "Initial release for soft launch testing"
7. Check **"Set as the latest release"**
8. Click **"Publish release"**

### Via Command Line

```bash
# Create and push tag
git tag -a v1.0-softlaunch -m "v1.0 Soft Launch"
git push origin v1.0-softlaunch

# Create release via GitHub CLI
gh release create v1.0-softlaunch --title "v1.0 Soft Launch" --notes "Initial release for soft launch testing"
```

---

## 📥 Creating a GitHub Release ZIP (Optional)

GitHub automatically creates ZIP files for releases:

1. Go to your repository
2. Click **Releases**
3. Click on any release
4. Download the **Source code (zip)** file

**Or** users can download directly:
- `https://github.com/YOUR_USERNAME/programming-foundations-course/archive/refs/tags/v1.0-softlaunch.zip`

---

## ✅ Verification Checklist

After setup, verify:

- [ ] Repository is created on GitHub
- [ ] All files are pushed (check GitHub web interface)
- [ ] Repository is set to **Private**
- [ ] Two testers are invited as collaborators
- [ ] Release tag `v1.0-softlaunch` is created
- [ ] Placeholders are documented in `PLACEHOLDERS-TO-FILL.md`

---

## 🔧 Troubleshooting

### "Git is not recognized"

**Problem:** Git command not found

**Solution:**
1. Install Git: https://git-scm.com/downloads
2. Restart terminal/PowerShell
3. Verify: `git --version`

### "Authentication failed"

**Problem:** Can't push to GitHub

**Solution:**
1. Use Personal Access Token instead of password
2. Create token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
3. Scopes needed: `repo` (full control)
4. Use token as password when pushing

### "Remote origin already exists"

**Problem:** Remote already configured

**Solution:**
```bash
# Remove existing remote
git remote remove origin

# Add correct remote
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### "Branch 'main' does not exist"

**Problem:** Branch name mismatch

**Solution:**
```bash
# Rename current branch to main
git branch -M main

# Push
git push -u origin main
```

---

## 📝 Next Steps After Setup

1. **Fill placeholders:**
   - Replace `[GITHUB_REPO_URL]` with your actual repo URL
   - Replace `[SUPPORT_EMAIL]` with your support email
   - See `PLACEHOLDERS-TO-FILL.md` for complete list

2. **Commit placeholder updates:**
   ```bash
   git add .
   git commit -m "Update placeholders with actual values"
   git push
   ```

3. **Share with testers:**
   - Send them the repository link
   - Point them to `TESTER-ACCESS.md`
   - Ask them to provide feedback

4. **Monitor feedback:**
   - Check GitHub Issues (if testers create them)
   - Check your support email
   - Make improvements based on feedback

---

## 🎯 Quick Reference Commands

```bash
# Check git status
git status

# See commit history
git log --oneline

# Push changes
git add .
git commit -m "Your commit message"
git push

# Pull updates (if working from multiple machines)
git pull

# View remote repository
git remote -v
```

---

**You're all set!** Your course is now on GitHub and ready for testers. 🚀

---

*Last updated: January 2024*

