"""A Program to Plan a Tea Party"""

__author__ = "730741801"


def main_planner(guests: int) -> None:
    """Function that calls each and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates amount of tea bags needed based on number of tea guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculate amount of treats needed based on number of tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
