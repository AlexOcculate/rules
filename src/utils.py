"""
Utilities for rule processing.

Common utilities used across the rule conversion tools.
"""

import re
import tomllib
from pathlib import Path
import yaml


def parse_frontmatter_and_content(content: str) -> tuple[dict | None, str]:
    """
    Parse YAML frontmatter and content from markdown.
    
    Frontmatter must be in the format:
        ---
        yaml content
        ---
        markdown content
    
    The closing --- must be on its own line (not part of a comment or text).

    Args:
        content: Full file content

    Returns:
        Tuple of (frontmatter dict, markdown content)
        Returns (None, content) if no valid frontmatter found
    """
    if not content.startswith("---\n"):
        return None, content

    # Look for closing --- on its own line
    # Use regex to ensure --- is at start of line (after newline)
    closing_pattern = re.compile(r'\n---\n')
    match = closing_pattern.search(content)
    
    if not match:
        # No proper closing ---, treat as no frontmatter
        return None, content
    
    # Extract frontmatter between opening and closing ---
    frontmatter_text = content[4:match.start()]  # Skip opening "---\n"
    markdown_content = content[match.end():]  # Skip closing "---\n"

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return None, content

    return frontmatter, markdown_content.strip()


def get_version_from_pyproject() -> str:
    """
    Read version from pyproject.toml using Python's built-in TOML parser.

    Requires Python 3.11+ for tomllib support.

    Returns:
        Version string from pyproject.toml

    Raises:
        FileNotFoundError: If pyproject.toml is not found
        ValueError: If version field is missing or invalid
    """
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")

    try:
        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)

        if "project" in data and "version" in data["project"]:
            version = data["project"]["version"]
            if isinstance(version, str) and version.strip():
                return version.strip()
        raise ValueError("Version field not found in pyproject.toml [project] section")
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Invalid TOML syntax in pyproject.toml: {str(e)}")
    except (FileNotFoundError, ValueError):
        raise
    except Exception as e:
        raise ValueError(f"Unexpected error reading pyproject.toml: {str(e)}")
