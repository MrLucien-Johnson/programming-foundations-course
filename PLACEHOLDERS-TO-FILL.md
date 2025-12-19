# Placeholders to Fill Before Launch

This document lists all placeholder tokens that need to be replaced with actual values before sharing the course.

---

## 🔴 Critical Placeholders (Must Fill)

### `[GITHUB_REPO_URL]`

**What it is:** Your GitHub repository URL

**Example:** `https://github.com/yourusername/programming-foundations-course`

**Found in:**
- `README.md` (line 122)
- `START-HERE.md` (line 40)
- `HOW-TO-USE.md` (line 54)
- `COURSE-LINKS.md` (line 88)
- `GUMROAD-DELIVERY-GITHUB.md` (multiple occurrences - 3 variants)
- `TESTER-ACCESS.md` (line 147)

**Action:** Replace with your actual GitHub repository URL after creating the repo.

---

### `[SUPPORT_EMAIL]`

**What it is:** Your support email address for course questions

**Example:** `support@yourdomain.com` or `yourname@gmail.com`

**Found in:**
- `README.md` (line 200)
- `START-HERE.md` (line 240)
- `HOW-TO-USE.md` (line 316)
- `COURSE-LINKS.md` (line 100)
- `TESTER-ACCESS.md` (lines 147, 234)
- `GUMROAD-DELIVERY-GITHUB.md` (multiple occurrences - 3 variants)

**Action:** Replace with your actual support email address.

---

## 🟡 Optional Placeholders

### `[GITHUB_RELEASE_URL]`

**What it is:** GitHub releases page URL (optional - only if using releases)

**Example:** `https://github.com/yourusername/repo-name/releases`

**Found in:**
- `GUMROAD-DELIVERY-GITHUB.md` (multiple occurrences - 3 variants)

**Action:** Optional - only fill if you plan to use GitHub Releases for downloads.

---

## 🟢 License Placeholders

### `[YEAR]`

**What it is:** Current year for copyright

**Example:** `2024`

**Found in:**
- `LICENSE` (line 3)

**Action:** Replace with current year (e.g., 2024).

---

### `[COPYRIGHT_HOLDER]`

**What it is:** Your name or organization name

**Example:** `Your Name` or `Your Company Name`

**Found in:**
- `LICENSE` (line 3)

**Action:** Replace with your name or organization name.

---

## 📝 Notion Hub Placeholders (Archive - Not Used)

**Note:** These are in `Notion-Hub/` folder which is marked as archive. You can ignore these unless you decide to use Notion delivery.

- `[NOTION_HUB_LINK]` - Notion hub link
- `[PYTHON_ZIP_LINK]` - Python workbook ZIP download
- `[CSHARP_ZIP_LINK]` - C# workbook ZIP download
- `[BUNDLE_ZIP_LINK]` - Bundle ZIP download
- `[MODULE_XX_LINK]` - Module links (various)
- `[PYTHON_CHALLENGE_LINK]` - Python assessment link
- `[CSHARP_CHALLENGE_LINK]` - C# assessment link
- `[CERTIFICATE_DOWNLOAD_LINK]` - Certificate download link
- `[DATE]` - Date placeholders
- `[VERSION]` - Version placeholders

**Action:** Ignore these - they're in archived Notion files.

---

## ✅ Quick Fill Checklist

Before sharing the course:

- [ ] Replace all `[GITHUB_REPO_URL]` with your actual repo URL
- [ ] Replace all `[SUPPORT_EMAIL]` with your support email
- [ ] (Optional) Replace `[GITHUB_RELEASE_URL]` if using releases
- [ ] Replace `[YEAR]` in LICENSE with current year
- [ ] Replace `[COPYRIGHT_HOLDER]` in LICENSE with your name/org

---

## 🔍 How to Find and Replace

### Using VS Code / Cursor:

1. Press `Ctrl+Shift+H` (Windows/Linux) or `Cmd+Shift+H` (Mac)
2. Enter placeholder in "Find" field (e.g., `[GITHUB_REPO_URL]`)
3. Enter replacement in "Replace" field
4. Click "Replace All" or review each occurrence

### Using Command Line (PowerShell):

```powershell
# Replace in all files (be careful!)
Get-ChildItem -Recurse -File | ForEach-Object {
    (Get-Content $_.FullName) -replace '\[GITHUB_REPO_URL\]', 'https://github.com/yourusername/repo' | Set-Content $_.FullName
}
```

**Recommendation:** Use VS Code/Cursor find-and-replace for safety and review.

---

*Last updated: January 2024*

