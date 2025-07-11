"""Mutating functions."""

__author__ = "730546256"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(lst: list[int], item: int) -> None:
    """Mutates a list by appending an item to the end."""
    index: int = len(lst)
    lst[index:index] = [item]


def double(lst: list[int]) -> None:
    """Mutates a list by doubling each value."""
    index: int = 0
    while index < len(lst):
        lst[index] *= 2
        index += 1


double(list_2)
print(list_1)
print(list_2)
