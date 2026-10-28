import random as rd;
import typing as tp;



NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan",
         "Fiona", "George", "Hannah", "Isaac", "Julia"]

ACTIONS = ["swimming", "sleeping", "running", "dancing", "reading",
           "cooking", "skating", "singing", "jumping", "writing"]


def get_event():
    action = rd.choice(ACTIONS)
    name = rd.choice(NAMES)
    yield (name, action)


def main():
    for c in range(1, 1000):
        name, action = get_event()
        print(f"Event {c}: Player {name} did action {action}")
    


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
