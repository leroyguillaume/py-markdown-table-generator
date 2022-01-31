"""Markdown table generator"""

from typing import Dict


def generate_table(
    data: Dict[str, str]
) -> str:
    """Generate Markdown table from data.

    Keyword arguments:
    data -- dict with key as column header and value as cell
    """
    print(data)
    return "table"
