def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed_description = ""
    if unit == "packets":
        seed_description = f"{quantity} packets available"
    elif unit == "grams":
        seed_description = f"{quantity} grams total"
    elif unit == "area":
        seed_description = f"covers {quantity} square meters"
    else:
        seed_description = "Unknown unit type"
    print(f"{seed_type.capitalize()} seeds: {seed_description}")
