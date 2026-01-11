---
name: analyze-usage
description: Analyze component usage across the codebase with deprecation planning and migration impact analysis
allowed-tools:
  - Read
  - Write
  - Bash
  - Grep
  - Glob
argument-hint: "[component-name] [--deprecate] [--unused] [--adoption]"
---

# Analyze Component Usage

Analyze how components are used across your codebase. Track usage, plan deprecations, find unused components, and monitor adoption.

## Usage

```bash
# Analyze specific component
/analyze-usage Button

# Deprecation impact analysis
/analyze-usage Button@v1 --deprecate

# Find all unused components
/analyze-usage --unused

# Track adoption of new version
/analyze-usage Button@v2 --adoption
```

## What This Command Does

1. **Component Usage** (default):
   - Scans codebase for component imports
   - Reports usage statistics
   - Groups by feature, variant, file
   - Shows recent changes and migration status

2. **Deprecation Analysis** (`--deprecate`):
   - Analyzes impact of deprecating a component
   - Estimates migration effort (low/medium/high)
   - Lists breaking changes
   - Calculates estimated hours
   - Generates migration recommendations

3. **Unused Detection** (`--unused`):
   - Finds components with zero or low usage
   - Categorizes as safe-to-remove, potentially-unused, or low-usage
   - Estimates bundle size savings
   - Recommends removal candidates

4. **Adoption Tracking** (`--adoption`):
   - Tracks migration progress to new version
   - Shows adoption trends over time
   - Identifies migration blockers
   - Recommends next actions

## Instructions

Follow the component-usage-analytics skill for implementation details.

For detailed implementation, see: `skills/component-usage-analytics/SKILL.md`
