"""Cozy Tea Planning Exercise"""

__author__: str = "730558518"


def main_planner(guests: int) -> None:
    """Main planner function"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)) + "")
    print("Treats: " + str(treats(people=guests)) + "")
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
        + ""
    )


def tea_bags(people: int) -> int:
    """Number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
