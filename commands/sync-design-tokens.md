---
name: sync-design-tokens
description: Synchronize design tokens bidirectionally between Figma and code with automatic drift detection and conflict resolution
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - AskUserQuestion
argument-hint: "[--setup] [--check] [--from-figma] [--to-figma]"
---

# Sync Design Tokens

Synchronize design tokens between Figma and your codebase. Supports bidirectional sync, drift detection, and conflict resolution.

## Usage

```bash
# Initial setup
/sync-design-tokens --setup

# Check for drift (no changes applied)
/sync-design-tokens --check

# Sync from Figma to code only
/sync-design-tokens --from-figma

# Sync from code to Figma only
/sync-design-tokens --to-figma

# Bidirectional sync (default)
/sync-design-tokens
```

## What This Command Does

1. **Setup Mode** (`--setup`):
   - Configures Figma API connection
   - Installs dependencies
   - Creates Style Dictionary config
   - Sets up sync scripts
   - Performs initial token sync

2. **Check Mode** (`--check`):
   - Compares Figma and code tokens
   - Reports drift without making changes
   - Useful for CI/CD validation

3. **Sync Modes**:
   - `--from-figma`: Pull tokens from Figma, update code
   - `--to-figma`: Push code tokens to Figma
   - No flag: Bidirectional sync with conflict detection

## Instructions

Follow the design-token-sync skill for implementation details. Key steps:

1. Ask user for Figma file URL and access token
2. Install @figma/rest-api-client and style-dictionary
3. Create token sync scripts
4. Fetch tokens from Figma
5. Compare with code tokens
6. Apply changes based on mode
7. Generate output formats (CSS, SCSS, TS)

For detailed implementation, see: `skills/design-token-sync/SKILL.md`
