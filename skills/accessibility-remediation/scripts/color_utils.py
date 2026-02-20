#!/usr/bin/env python3
"""
Shared color utility functions for accessibility analysis and fix generation.

Provides hex color manipulation and WCAG contrast ratio calculation.
"""

from typing import Tuple


def hex_to_rgb(color: str) -> Tuple[int, int, int]:
    """Convert hex color string to RGB tuple"""
    color = color.lstrip("#")
    if len(color) == 3:
        color = "".join([c * 2 for c in color])
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def relative_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance per WCAG 2.2 definition"""
    r, g, b = [c / 255.0 for c in rgb]
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(fg: str, bg: str) -> float:
    """
    Calculate WCAG contrast ratio between two hex colors.

    Returns a default passing value (5.0) for non-hex or unparseable colors.
    """
    try:
        if fg.startswith("#") and bg.startswith("#"):
            l1 = relative_luminance(hex_to_rgb(fg))
            l2 = relative_luminance(hex_to_rgb(bg))
            lighter = max(l1, l2)
            darker = min(l1, l2)
            return (lighter + 0.05) / (darker + 0.05)
        return 5.0
    except (ValueError, ZeroDivisionError, TypeError):
        return 5.0


def darken_color(color: str, factor: float = 0.7) -> str:
    """Darken a hex color by reducing RGB values. Returns safe default on failure."""
    if not color.startswith("#"):
        return "#666"
    try:
        r, g, b = hex_to_rgb(color)
        r = max(0, int(r * factor))
        g = max(0, int(g * factor))
        b = max(0, int(b * factor))
        return f"#{r:02x}{g:02x}{b:02x}"
    except (ValueError, IndexError):
        return "#666"


def lighten_color(color: str, factor: float = 0.3) -> str:
    """Lighten a hex color by blending toward white. Returns safe default on failure."""
    if not color.startswith("#"):
        return "#f5f5f5"
    try:
        r, g, b = hex_to_rgb(color)
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f"#{r:02x}{g:02x}{b:02x}"
    except (ValueError, IndexError):
        return "#f5f5f5"
