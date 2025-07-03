"""Supplies for a tea party."""

__author__: str = "730546256"


def main_planner(guests: int) -> None:
    """Main function to plan items and costs for a tea party."""

    tea_count: int = tea_bags(guests)
    treat_count: int = treats(guests)
    total_cost: float = cost(tea_count, treat_count)
    # When trying to interact with my code I kept getting an error message, but it was due to the indentation being incorrect.
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea bags: {tea_count}")
    print(f"Treats: {treat_count}")
    print(f"Cost: ${total_cost}")


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for a tea party."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed for a tea party."""
    return int(tea_bags(people=people) * 1.5)


# it took me a while to figure out how to change the float to an integer, but I referred to my notes


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of tea bags and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
