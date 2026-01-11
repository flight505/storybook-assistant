---
name: help
description: Show all available Storybook Assistant features, commands, and capabilities with usage examples
allowed-tools:
  - Read
argument-hint: "[feature-name]"
---

# Storybook Assistant Help

Show comprehensive help for the Storybook Assistant Plugin, including all features, commands, and capabilities.

## Usage

```bash
# Show all features
/help

# Get help for specific feature
/help visual-regression
/help accessibility
/help design-to-code
```

## Instructions

When the user runs `/help`, provide a comprehensive, well-organized overview of the plugin's capabilities.

### Main Help Output

```markdown
# 🎨 Storybook Assistant Plugin v2.1.0

Your complete AI-powered Storybook development toolkit with SOTA 2026 features.

---

## 🚀 Quick Start Commands

### Setup & Configuration
- `/setup-storybook` - Initialize Storybook 9 with automatic framework detection
- `/setup-ci-cd` - Generate CI/CD pipeline with GitHub Actions
- `/setup-visual-testing` - Configure AI-powered visual regression testing

### Component Development
- `/create-component` - Scaffold new component with stories and tests
- `/generate-stories` - Generate stories for existing components
- `/design-to-code` - Transform design screenshots into React components (Vision AI)
- `/generate-from-description` - Create components from natural language

### Quality & Testing
- `/fix-accessibility` - AI-powered accessibility remediation with one-click fixes
- `/generate-dark-mode` - Auto-generate dark mode color schemes

### Maintenance & Analytics
- `/sync-design-tokens` - Sync design tokens between Figma and code
- `/analyze-usage` - Analyze component usage and plan deprecations

---

## 📚 All Features (17 Skills)

### Original Features (7)
1. **storybook-config** - Storybook 9 setup and configuration
2. **story-generation** - Generate story files with tests
3. **component-scaffold** - Scaffold components with stories
4. **visual-design** - Generate style guides and mockups
5. **testing-suite** - Comprehensive testing setup
6. **platform-support** - Tauri/Electron support
7. **style-guide-generator** - Design system documentation

### SOTA 2026 Features (10)
8. **design-to-code** 🎨 - Vision AI: Screenshots → Components
9. **natural-language-generation** 💬 - English → Components
10. **accessibility-remediation** ♿ - AI-powered a11y fixes
11. **server-components** 🌐 - React 19 Server Components
12. **visual-regression-testing** 🔍 - Intelligent diff analysis
13. **design-token-sync** 🔄 - Figma ↔ Code synchronization
14. **component-usage-analytics** 📊 - Usage tracking & deprecation
15. **dark-mode-generation** 🌓 - Auto-generate dark themes
16. **performance-analysis** ⚡ - Bundle optimization
17. **ci-cd-generator** 🔧 - Pipeline generation

---

## 🤖 Autonomous Agents (3)

These agents work independently to analyze and fix issues:

1. **accessibility-auditor** - Scans components for WCAG violations
2. **component-generator** - Generates components from descriptions
3. **visual-regression-analyzer** - Analyzes visual diffs with AI

---

## 💡 Common Workflows

### Workflow 1: New Component from Design
```bash
1. /design-to-code [upload screenshot]
2. /fix-accessibility ComponentName
3. /generate-dark-mode ComponentName
4. /setup-visual-testing
```

### Workflow 2: Improve Existing Component
```bash
1. /generate-stories ComponentName
2. /fix-accessibility ComponentName
3. /analyze-usage ComponentName
```

### Workflow 3: Design System Sync
```bash
1. /sync-design-tokens --setup
2. /sync-design-tokens (regular sync)
3. /setup-visual-testing (detect changes)
```

### Workflow 4: Full Project Setup
```bash
1. /setup-storybook
2. /setup-ci-cd
3. /setup-visual-testing
4. /sync-design-tokens --setup
```

---

## 🎯 Feature Highlights

### 🏆 Flagship: Vision AI Design-to-Code
Transform screenshots into pixel-perfect components:
- Extracts spacing, colors, typography automatically
- Generates design tokens
- Creates multiple variants
- Full TypeScript support

**Example:** `/design-to-code ./designs/button.png`

### ♿ Accessibility Remediation
AI-powered WCAG 2.2 compliance:
- Context-aware fix suggestions
- One-click application
- Ranked recommendations (Best → Good → Acceptable)
- Real-time detection via hooks

**Example:** `/fix-accessibility Button.tsx`

### 🔍 Visual Regression Testing
Intelligent screenshot comparison:
- 90% reduction in false positives
- Context-aware (git history, design tokens)
- Auto-approval rules
- CI/CD integration

**Example:** `/setup-visual-testing`

### 🔄 Design Token Sync
Bidirectional Figma synchronization:
- Automatic drift detection
- Conflict resolution
- Multi-format output (CSS, SCSS, TS, JSON)
- Style Dictionary integration

**Example:** `/sync-design-tokens --setup`

### 📊 Component Analytics
Data-driven component management:
- Usage tracking across codebase
- Deprecation impact analysis
- Unused component detection
- Migration effort estimation

**Example:** `/analyze-usage Button`

---

## 🆘 Getting Help

### For Specific Features
- `/help visual-regression` - Visual regression testing guide
- `/help accessibility` - Accessibility features
- `/help design-to-code` - Vision AI usage
- `/help tokens` - Design token sync

### Documentation
- **Quick Start:** See README.md
- **SOTA Features:** See SOTA_IMPLEMENTATION_COMPLETE.md
- **Roadmap:** See SOTA_ROADMAP_2026.md

### Troubleshooting
- Missing API keys? Check CLAUDE_CODE_OAUTH_TOKEN and OPENROUTER_API_KEY
- Command not found? Verify plugin is enabled: `claude --plugins`
- Need examples? Each skill has examples/ directory

---

## 🔧 Requirements

**Required:**
- Node.js ≥ 20.0.0
- npm ≥ 10.0.0
- CLAUDE_CODE_OAUTH_TOKEN or ANTHROPIC_API_KEY

**Optional (for visual generation):**
- OPENROUTER_API_KEY - AI-powered visual assets

---

## 📖 Quick Reference

### Most Used Commands
```bash
/setup-storybook              # First-time setup
/generate-stories             # Add stories to components
/design-to-code               # Screenshot → Component
/fix-accessibility            # Fix a11y issues
/setup-visual-testing         # Visual regression
```

### Ask Questions
You can also just ask me naturally:
- "How do I set up Storybook?"
- "Generate a button component from this description"
- "Fix accessibility issues in my Card component"
- "Show me how to sync design tokens"
- "Analyze usage of the Button component"

---

**Version:** 2.1.0
**Total Features:** 17 skills, 3 agents, 11 commands
**Status:** Production Ready ✅

For detailed documentation on any feature, just ask or type `/help [feature-name]`
```

### Feature-Specific Help

When user requests help for a specific feature, read the corresponding SKILL.md file and provide a concise summary with:

1. **What it does** - Brief overview
2. **When to use** - Common scenarios
3. **How to use** - Command examples
4. **Key features** - Bullet list of capabilities
5. **Related features** - Other relevant skills/commands

**Example for `/help visual-regression`:**

```markdown
# 🔍 AI-Powered Visual Regression Testing

## What It Does
Intelligently analyzes visual differences between baseline and current screenshots to distinguish intentional design changes from actual bugs.

## When to Use
- Setting up visual regression testing
- Reviewing visual changes in PRs
- Detecting UI regressions
- Reducing false positives from pixel diffs

## How to Use
```bash
# Initial setup
/setup-visual-testing

# Run tests
npm run test:visual

# Interactive review
npm run test:visual:interactive

# Update baselines
npm run test:visual:update
```

## Key Features
✅ 90% reduction in false positives vs traditional pixel diff
✅ Context-aware analysis (git commits, design tokens)
✅ Auto-approval for expected changes (theme updates, etc.)
✅ Categorizes changes: Ignore, Expected, Warning, Error
✅ CI/CD integration with GitHub Actions
✅ Works with Chromatic/Percy

## How It Works
1. Captures screenshots of all Storybook stories
2. Compares with baseline screenshots
3. AI analyzes differences with context (git history, tokens)
4. Categorizes intelligently:
   - **Ignore:** Rendering noise, anti-aliasing
   - **Expected:** Matches design token updates
   - **Warning:** Significant but might be intentional
   - **Error:** Clear regressions (layout shifts, broken UI)

## Related Features
- `testing-suite` - Interaction and accessibility tests
- `design-token-sync` - Validate token changes visually
- `ci-cd-generator` - Add visual tests to CI pipeline

For full documentation: `skills/visual-regression-testing/SKILL.md`
```

### Natural Language Queries

If the user asks questions naturally (not using /help command), provide helpful responses:

**User:** "What can this plugin do?"
**Response:** Show main help output with all features

**User:** "How do I fix accessibility issues?"
**Response:** Explain accessibility-remediation skill and /fix-accessibility command

**User:** "Can you help me with visual regression testing?"
**Response:** Provide visual-regression-testing specific help

**User:** "Show me all commands"
**Response:** List all 11 commands with brief descriptions

---

## Implementation Notes

1. **Always read the actual SKILL.md** when providing feature-specific help
2. **Use examples** - Show concrete command usage
3. **Link related features** - Help users discover connections
4. **Keep it concise** - Summaries, not walls of text
5. **Encourage exploration** - Point to full documentation files

The help system should make the plugin approachable and discoverable for new users while providing quick reference for experienced users.
