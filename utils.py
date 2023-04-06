from typing import Any


def pa(value: Any):
    """Print and return a string."""
    from pprint import pprint
    pprint(value)
    return value
