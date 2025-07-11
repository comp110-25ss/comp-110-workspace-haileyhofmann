"""While Loops Practice"""

__author__ = "730546256"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of instances of a character in a string."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
