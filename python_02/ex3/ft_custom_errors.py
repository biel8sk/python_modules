class GardenError(Exception):
    def __init__(self, mensagem=None):
        super().__init__(mensagem or "Unknown plant error")


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_operations(operations_number):
    if (operations_number == "PlantError"):
        raise PlantError("The tomato plant is wilting")
    elif (operations_number == "WaterError"):
        raise WaterError("Not enough water in the tank!")
    else:
        raise GardenError("The tomato plant is wilting")


def test_error_types():
    print("=== Garden Error Types Demo ===", end="\n\n")
    for data in ["PlantError", "WaterError", "GardenError"]:
        print(f"Testing : {data}...")
        try:
            garden_operations(data)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_error_types()
