def garden_operations(operations_number):
    if (operations_number == 0):
        1 + "3"
    elif (operations_number == 1):
        int("str")
    elif (operations_number == 2):
        open("filenotfound")
    elif (operations_number == 3):
        2 / 0
    else:
        print("Operation completed successfully")


def test_error_types():
    print("=== Garden Error Types Demo ===", end="\n\n")
    for data in [0, 1, 2, 3, 4]:
        print(f"Testing operation: {data}...")
        try:
            garden_operations(data)
        except Exception as e:
            print(f"Caught: {e.__class__.__name__} {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_error_types()
