# Versioning Rules: Programming Foundations Course

## 📋 Version Number Format

**Format:** `vMAJOR.MINOR.PATCH`

Examples:
- `v1.0` - Initial launch
- `v1.1` - Minor update (new content, improvements)
- `v1.2` - Another minor update
- `v2.0` - Major update (significant additions)
- `v2.1` - Minor update after major release

---

## 🎯 Version Number Guidelines

### MAJOR Version (v2.0, v3.0)

**Increase when:**
- Adding entirely new modules or tracks
- Major restructuring of course content
- Significant new features (video content, interactive elements)
- Breaking changes that require re-downloading workbooks

**Examples:**
- Adding a JavaScript track → v2.0
- Complete course redesign → v2.0
- Adding video lessons → v2.0

### MINOR Version (v1.1, v1.2)

**Increase when:**
- Adding new examples or exercises
- Improving explanations or clarity
- Adding new features to existing modules
- Expanding portfolio guide or assessments
- Adding new FAQ entries

**Examples:**
- Adding 2 new exercises to Module 3 → v1.1
- Improving Module 2 explanations → v1.1
- Adding new portfolio examples → v1.2

### PATCH Version (v1.0.1, v1.0.2)

**Increase when:**
- Fixing typos or errors
- Correcting code examples
- Fixing broken links
- Small clarifications
- Bug fixes in provided code

**Examples:**
- Fixing typo in Module 1 → v1.0.1
- Correcting code example → v1.0.1
- Fixing broken link → v1.0.2

---

## 📝 Changelog Entry Rules

### For Each Update, Document:

**Added:**
- New content, examples, exercises
- New modules or features
- New resources or guides

**Improved:**
- Better explanations
- Clearer instructions
- Enhanced examples
- Improved organization

**Fixed:**
- Errors or typos
- Broken code
- Incorrect information
- Broken links

**Changed:**
- Modifications to existing content
- Restructured sections
- Updated recommendations

---

## 🔄 Update Frequency Guidelines

### Major Updates (v2.0+)

- **Frequency:** Rarely (every 6-12 months, if at all)
- **Announcement:** Significant announcement
- **Action Required:** Re-download workbook recommended

### Minor Updates (v1.x)

- **Frequency:** As needed (monthly or quarterly)
- **Announcement:** Changelog update
- **Action Required:** Optional re-download, check changelog

### Patch Updates (v1.0.x)

- **Frequency:** As needed (when errors found)
- **Announcement:** Changelog update
- **Action Required:** Optional, check changelog

---

## 📢 How to Announce Updates

### For Major Updates (v2.0+)

**Announcement should include:**
- What's new (major features)
- Why it matters (benefits to learners)
- What learners need to do (re-download, etc.)
- Timeline (when available)

**Channels:**
- Email to all buyers
- Notion hub announcement
- Changelog update
- Social media (if applicable)

### For Minor Updates (v1.x)

**Announcement should include:**
- What's new (new content, improvements)
- Where to find it (which modules)
- Optional: What learners might want to check out

**Channels:**
- Changelog update
- Notion hub changelog
- Optional: Email to recent buyers

### For Patch Updates (v1.0.x)

**Announcement should include:**
- What was fixed
- Where it was (which module/page)
- No action required (usually)

**Channels:**
- Changelog update only
- No need for major announcement

---

## ✅ Version Update Checklist

Before releasing an update:

- [ ] Version number incremented correctly
- [ ] Changelog updated with all changes
- [ ] All files updated consistently
- [ ] Links checked and working
- [ ] Code examples tested
- [ ] No typos or errors introduced
- [ ] Update announcement prepared (if needed)
- [ ] Notion hub updated (if applicable)

---

## 🎯 Versioning Best Practices

### Do's ✅

- **Be consistent** - Follow the format
- **Document everything** - Update changelog
- **Test updates** - Make sure everything works
- **Communicate clearly** - Tell learners what changed
- **Be honest** - Don't overhype minor updates

### Don'ts ❌

- **Don't skip versions** - Go from v1.0 to v1.2 (unless v1.1 was internal)
- **Don't forget changelog** - Always document changes
- **Don't break things** - Test before releasing
- **Don't over-announce** - Patch updates don't need fanfare
- **Don't change version format** - Keep it consistent

---

## 📊 Version History Template

When creating a new version entry in Changelog:

```markdown
## Version X.Y - [Title]

**Release Date:** [DATE]

**What's New:**
- Added: [New content]
- Improved: [Better explanations]
- Fixed: [Bug fixes]
- Changed: [Modifications]

**Details:**
- [Specific changes]
- [Which modules affected]
- [What learners should know]
```

---

## 🔍 Version Tracking

### Where to Update Version Numbers

1. **Changelog.md** - Add new version entry
2. **Notion Hub pages** - Update footer version numbers
3. **Workbook README files** - Update version if major
4. **Sales page** - Update if major version
5. **Gumroad product** - Update description if major

### Version Number Locations

- Footer of Notion pages: `Version: [VERSION]`
- Changelog header: `Current Version: [VERSION]`
- Workbook README: `Version: [VERSION]` (if included)

---

## 💡 Versioning Philosophy

**Keep it simple:**
- Don't overcomplicate versioning
- Focus on what matters to learners
- Major = significant changes
- Minor = improvements/additions
- Patch = fixes

**Be transparent:**
- Always document changes
- Explain what's new
- Tell learners what to do (if anything)

**Stay consistent:**
- Use the same format
- Update changelog every time
- Communicate clearly

---

*This versioning system keeps updates organized and helps learners understand what's changed and why.*

