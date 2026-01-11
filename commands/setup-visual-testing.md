---
name: setup-visual-testing
description: Set up AI-powered visual regression testing for Storybook with intelligent diff analysis and auto-approval rules
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - AskUserQuestion
argument-hint: "[--chromatic] [--percy]"
---

# Setup Visual Regression Testing

Set up AI-powered visual regression testing for your Storybook project. This command configures intelligent visual diff analysis that understands the difference between intentional design changes and actual bugs.

## What This Command Does

1. **Detects your environment**
   - Framework (React, Vue, Svelte, etc.)
   - Build tool (Vite, Webpack)
   - Existing visual testing tools (Chromatic, Percy)
   - CI/CD provider (GitHub Actions, GitLab, CircleCI)

2. **Asks for your preferences**
   - Integration with Chromatic/Percy (optional)
   - Auto-approval rules
   - Pixel difference threshold
   - CI/CD integration

3. **Installs dependencies**
   - `@storybook/test-runner`
   - `playwright`
   - `pixelmatch` (for pixel diff)
   - Python dependencies (for AI analysis)

4. **Creates configuration files**
   - `.storybook/test-runner-config.ts` - Test runner setup
   - `.storybook/visual-regression.config.ts` - AI analysis config
   - `scripts/visual-regression/analyze_diff.py` - AI analysis engine
   - `.github/workflows/visual-regression.yml` - CI integration (optional)

5. **Captures baseline screenshots**
   - Renders all Storybook stories
   - Takes screenshots of each variant
   - Stores baselines in `.storybook/visual-baselines/`

6. **Sets up NPM scripts**
   - `npm run test:visual` - Run visual regression tests
   - `npm run test:visual:update` - Update baselines
   - `npm run test:visual:interactive` - Interactive review mode

## Usage

```bash
# Basic setup
/setup-visual-testing

# With Chromatic integration
/setup-visual-testing --chromatic

# With Percy integration
/setup-visual-testing --percy
```

## Instructions

### Step 1: Detect Environment

Read the user's project to detect:
- Framework and build tool
- Existing Storybook configuration
- Current testing setup
- CI/CD configuration

```bash
# Check package.json for dependencies
# Check .storybook/main.ts for configuration
# Check .github/workflows for CI setup
```

### Step 2: Ask User Preferences

Use AskUserQuestion to clarify:

1. **Integration preference**:
   - "Standalone (recommended)" - Pure AI analysis
   - "Chromatic integration" - Combine with Chromatic
   - "Percy integration" - Combine with Percy

2. **Auto-approval rules**:
   - "Conservative (manual review)" - Approve nothing automatically
   - "Balanced (recommended)" - Auto-approve token changes, anti-aliasing
   - "Aggressive (CI-friendly)" - Auto-approve most changes

3. **CI/CD integration**:
   - "Yes" - Set up GitHub Actions workflow
   - "No" - Manual testing only

### Step 3: Install Dependencies

```bash
npm install --save-dev @storybook/test-runner playwright pixelmatch
npx playwright install chromium
```

If Python scripts needed:
```bash
pip install Pillow anthropic python-dotenv
```

### Step 4: Create Test Runner Configuration

Create `.storybook/test-runner-config.ts`:

```typescript
import { getStoryContext } from '@storybook/test-runner';
import { analyzeVisualDiff } from './visual-regression-ai';
import { compareImages } from './visual-regression-utils';

export default {
  async postRender(page, context) {
    const storyContext = await getStoryContext(page, context);
    const storyId = context.id;

    // Capture screenshot
    const screenshot = await page.screenshot({ fullPage: true });

    // Compare with baseline
    const baselinePath = `.storybook/visual-baselines/${storyId}.png`;
    const diff = await compareImages(baselinePath, screenshot);

    if (diff && diff.pixelsChanged > 0) {
      // AI analysis
      const analysis = await analyzeVisualDiff({
        diff,
        storyId,
        componentName: storyContext.component,
        baselinePath,
        currentScreenshot: screenshot,
      });

      // Handle based on AI categorization
      if (analysis.category === 'error') {
        throw new Error(
          `Visual regression detected in ${storyId}:\\n${analysis.message}`
        );
      } else if (analysis.category === 'warning') {
        console.warn(
          `Visual change detected in ${storyId}: ${analysis.message}`
        );
      }
      // 'expected' and 'ignore' categories pass silently
    }
  },
};
```

### Step 5: Create AI Analysis Configuration

Create `.storybook/visual-regression.config.ts`:

```typescript
export default {
  // Pixel difference threshold (0-1)
  threshold: 0.01, // 1% difference triggers analysis

  // Auto-approval rules
  autoApprove: {
    tokenChanges: true,      // Auto-approve design token updates
    antiAliasing: true,      // Ignore anti-aliasing differences
    timestamps: true,        // Ignore timestamp changes
    uuids: true,            // Ignore UUID changes
  },

  // AI analysis settings
  aiAnalysis: {
    includeGitHistory: true,
    includePRDescription: true,
    includeDesignTokens: true,
    lookbackDays: 7,
  },

  // Categorization thresholds
  thresholds: {
    ignore: 0.001,    // < 0.1% = ignore
    expected: 0.01,   // < 1% = expected
    warning: 0.05,    // < 5% = warning
    error: 0.05,      // >= 5% = error
  },

  // Notification settings
  notifications: {
    onError: 'always',
    onWarning: 'pr-only',
    onSuccess: 'never',
  },

  // Baseline storage
  baselinePath: '.storybook/visual-baselines/',

  // Cloud storage (optional)
  cloudStorage: {
    provider: null, // 'chromatic', 'percy', 's3', null
    config: {},
  },
};
```

### Step 6: Create Analysis Scripts

Create `scripts/visual-regression/analyze_diff.py` using the implementation from the visual-regression-testing skill.

Key functions:
- `analyze_with_context(diff, baseline, context)` - Main analysis
- `categorize_change(change, context)` - Categorization logic
- `check_token_match(old_color, new_color)` - Token validation
- `get_recent_commits()` - Git history
- `load_design_tokens()` - Token system

### Step 7: Create Helper Utilities

Create `.storybook/visual-regression-utils.ts`:

```typescript
import { PNG } from 'pngjs';
import pixelmatch from 'pixelmatch';
import fs from 'fs/promises';

export async function compareImages(
  baselinePath: string,
  currentScreenshot: Buffer
): Promise<{ pixelsChanged: number; diffImage: Buffer } | null> {
  try {
    // Read baseline
    const baselineBuffer = await fs.readFile(baselinePath);
    const baseline = PNG.sync.read(baselineBuffer);
    const current = PNG.sync.read(currentScreenshot);

    // Ensure same dimensions
    if (baseline.width !== current.width || baseline.height !== current.height) {
      throw new Error('Image dimensions do not match');
    }

    // Create diff image
    const diff = new PNG({ width: baseline.width, height: baseline.height });

    // Compare
    const pixelsChanged = pixelmatch(
      baseline.data,
      current.data,
      diff.data,
      baseline.width,
      baseline.height,
      { threshold: 0.1 }
    );

    return {
      pixelsChanged,
      diffImage: PNG.sync.write(diff),
    };
  } catch (error) {
    // Baseline doesn't exist - first run
    return null;
  }
}

export async function saveBaseline(storyId: string, screenshot: Buffer) {
  const path = `.storybook/visual-baselines/${storyId}.png`;
  await fs.writeFile(path, screenshot);
}
```

### Step 8: Add NPM Scripts

Update `package.json`:

```json
{
  "scripts": {
    "test:visual": "test-storybook",
    "test:visual:update": "test-storybook --updateSnapshots",
    "test:visual:interactive": "test-storybook --watch",
    "test:visual:ci": "test-storybook --ci"
  }
}
```

### Step 9: Capture Initial Baselines

```bash
# Build Storybook
npm run build-storybook

# Run test runner to capture baselines
npm run test:visual:update
```

Output:
```
Capturing baseline screenshots...
  ✓ Button/Primary
  ✓ Button/Secondary
  ✓ Card/Default
  ✓ Card/WithImage
  ...
  ✓ Captured 47 stories

Baselines saved to .storybook/visual-baselines/
```

### Step 10: CI/CD Integration (Optional)

If user wants CI integration, create `.github/workflows/visual-regression.yml`:

```yaml
name: Visual Regression Testing

on:
  pull_request:
    branches: [main, develop]

jobs:
  visual-regression:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for git analysis

      - uses: actions/setup-node@v3
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright browsers
        run: npx playwright install chromium

      - name: Build Storybook
        run: npm run build-storybook

      - name: Run visual regression tests
        run: npm run test:visual:ci
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

      - name: Upload visual regression report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: visual-regression-report
          path: .storybook/visual-regression-report/

      - name: Comment PR
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '⚠️ Visual regression tests failed. See [report](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}) for details.'
            })
```

### Step 11: Create Documentation

Create `.storybook/VISUAL_TESTING.md`:

```markdown
# Visual Regression Testing

This project uses AI-powered visual regression testing to catch UI bugs.

## Running Tests

\`\`\`bash
# Run tests
npm run test:visual

# Interactive mode (review changes)
npm run test:visual:interactive

# Update baselines
npm run test:visual:update
\`\`\`

## How It Works

1. Captures screenshots of all Storybook stories
2. Compares with baseline screenshots
3. AI analyzes differences with context (git, design tokens)
4. Categorizes as: ignore, expected, warning, or error

## Auto-Approval Rules

The AI automatically approves:
- Design token updates
- Anti-aliasing differences
- Timestamp changes

Layout shifts and unexpected color changes require manual review.

## Configuration

Edit `.storybook/visual-regression.config.ts` to adjust:
- Pixel difference threshold
- Auto-approval rules
- AI analysis settings
```

### Step 12: Final Summary

Present to user:

```
✅ Visual Regression Testing Setup Complete!

Configured:
  ✓ AI-powered diff analysis
  ✓ Baseline screenshots (47 stories)
  ✓ Auto-approval rules (balanced)
  ✓ NPM scripts
  ✓ CI/CD integration (GitHub Actions)

Next Steps:
1. Make a change to a component
2. Run: npm run test:visual
3. Review AI analysis results

Configuration:
  - Edit: .storybook/visual-regression.config.ts
  - Baselines: .storybook/visual-baselines/
  - Docs: .storybook/VISUAL_TESTING.md

Useful Commands:
  npm run test:visual              - Run tests
  npm run test:visual:interactive  - Interactive review
  npm run test:visual:update       - Update baselines
```

## Chromatic Integration

If user selected Chromatic:

1. Install Chromatic:
```bash
npm install --save-dev chromatic
```

2. Add to package.json:
```json
{
  "scripts": {
    "chromatic": "chromatic --project-token=<token>"
  }
}
```

3. Configure to work alongside AI analysis:
```typescript
// .storybook/visual-regression.config.ts
export default {
  cloudStorage: {
    provider: 'chromatic',
    config: {
      projectToken: process.env.CHROMATIC_PROJECT_TOKEN,
    },
  },
};
```

## Percy Integration

If user selected Percy:

1. Install Percy:
```bash
npm install --save-dev @percy/cli @percy/storybook
```

2. Add to package.json:
```json
{
  "scripts": {
    "percy": "percy storybook http://localhost:6006"
  }
}
```

3. Configure to work alongside AI analysis

## Error Handling

### Missing Anthropic API Key

If `ANTHROPIC_API_KEY` not set:
```
❌ Error: ANTHROPIC_API_KEY environment variable not set

AI-powered analysis requires Claude API access. Please:
1. Get API key from: https://console.anthropic.com/
2. Add to .env: ANTHROPIC_API_KEY=your_key_here
3. Or run with: ANTHROPIC_API_KEY=your_key npm run test:visual

Fallback: You can use traditional pixel diff without AI analysis.
Would you like to set up without AI? [Yes/No]
```

### No Baseline Screenshots

If baselines don't exist:
```
ℹ️ No baseline screenshots found. Capturing initial baselines...

This is the first run. All screenshots will be saved as baselines.
Future runs will compare against these baselines.

Run 'npm run test:visual:update' to refresh baselines after approved changes.
```

### Incompatible Storybook Version

If Storybook < 7:
```
❌ Error: Storybook 7+ required for visual regression testing

Your version: 6.5.16
Required: 7.0.0+

Please upgrade Storybook:
  npm install --save-dev @storybook/react@latest

Or use legacy visual testing with Percy/Chromatic.
```

## Tips for Success

1. **Commit baselines** - Add `.storybook/visual-baselines/` to git
2. **Update regularly** - Refresh baselines after approved visual changes
3. **Review warnings** - Don't ignore AI warnings, they might be real bugs
4. **Tune threshold** - Adjust pixel threshold if too many false positives
5. **Use interactive mode** - Review changes interactively during development

---

**Related Skills:**
- `visual-regression-testing` - Core AI analysis methodology
- `testing-suite` - Interaction and accessibility testing
- `ci-cd-generator` - CI/CD pipeline setup

**Related Commands:**
- `/setup-ci-cd` - Configure full CI/CD pipeline
- `/setup-storybook` - Initial Storybook setup
