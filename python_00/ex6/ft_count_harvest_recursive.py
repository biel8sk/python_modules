def count_recursive(day: int, limit: int):
    if day > limit:
        return
    print(f"Day: {day}")
    count_recursive(day+1, limit)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_recursive(1, days)
    print("Harvest time!")
