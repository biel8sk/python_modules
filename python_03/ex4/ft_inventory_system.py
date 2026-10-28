import sys as s


def get_max_abundant(itens: dict):
    if len(list(itens.values())) == 0:
        return ("", 0)
    max_item = 0
    key = ""
    for k in itens.keys():
        if max_item < itens[k]:
            max_item = itens[k]
            key = k
    return (key, max_item)


def get_min_abundant(itens: dict):
    if len(itens.values()) == 0:
        return ("", 0)
    min_item = list(itens.values())[0]
    key: str = list(itens.keys())[0]
    for k in itens.keys():
        if min_item > itens[k]:
            key = k
            min_item = itens[k]
    return (key, min_item)


def main() -> None:
    args: list[str] = s.argv[1:]
    itens: dict[str, int] = {}
    total = 0
    for arg in args:
        try:
            if (arg.count(':') != 1 or arg.strip(':').count(':') != 1):
                print(f"Error - invalid parameter '{arg}'")
                continue
            parts = arg.split(':')
            k = parts[0]
            if k in itens.keys():
                print(f"Redundant item '{k}' - discarding")
                continue
            v = int(parts[1])
            itens[k] = v
        except ValueError as ex:
            print(f"Quantity error for 'key': {ex}")
    keys = itens.keys()
    total = sum(itens.values())
    max_abundant = get_max_abundant(itens)
    min_abundant = get_min_abundant(itens)
    print(f"Got inventory: {itens}")
    print(f"Item list: {list(keys)}")
    print(f"Total quantity of the 5 items: {sum([itens[p] for p in keys])}")
    for i in itens.keys():
        print(f"Item {i} represents {((itens[i] * 100) / total):.1f}%")
    print(f"Item most abundant: {max_abundant[0]} "
          f"with quantity {max_abundant[1]}")
    print(f"Item least abundant: {min_abundant[0]} "
          f"with quantity {min_abundant[1]}")
    itens.update({"sword": 29})
    print(f"Updated inventory: {itens}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
