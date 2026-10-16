def input_temperature(temp_str):
    temp_int = int(temp_str)
    if (temp_int < 0):
        raise Exception(f"{temp_int}°C is too cold for plants (min 0°C)")
    if (temp_int > 40):
        raise Exception(f"{temp_int}°C is too hot for plants (max 40°C)")
    print(f"Temperature is now {temp_int}°C")
    return temp_int


def test_temperature():
    print("=== Garden Temperature Checker ===", end="\n\n")
    for data in ['100', '25', 'abc']:
        print(f"Input data is '{data}'")
        try:
            input_temperature(data)
        except Exception as e:
            print(f"Caught input temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
