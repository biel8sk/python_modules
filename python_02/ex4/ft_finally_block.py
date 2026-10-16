class GardenError(Exception):
    def __init__(self, mensagem=None):
        super().__init__(mensagem or "Unknown plant error")


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_names):
    print("Opening watering system")
    for plant in plant_names:
        if (str.capitalize(plant) != plant):
            raise PlantError(f"Invalid plant name to water: {plant}")
        print(f"Watering: {plant}  [OK]")


def test_watering_system(input, type):
    print(f"Testing {type} plants")
    try:
        water_plant(input)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main\n")
        return
    finally:
        print("Closing watering system")
        print("Cleanup always happens, even with errors!")


if __name__ == '__main__':
    print("=== Garden Watering System ===", end="\n\n")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce"]
    test_watering_system(valid_plants, "valid")
    print("")
    test_watering_system(invalid_plants, "invalid")
