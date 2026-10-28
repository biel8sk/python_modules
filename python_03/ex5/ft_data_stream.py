import random as rd;
import typing as tp;

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan",
         "Fiona", "George", "Hannah", "Isaac", "Julia"]
ACTIONS = ["swimming", "sleeping", "running", "dancing", "reading",
           "cooking", "skating", "singing", "jumping", "writing"]


def get_event() -> tp.Generator[tuple]:
    while True:
        action: str = rd.choice(ACTIONS)
        name: str = rd.choice(NAMES)
        yield (name, action)


def consume_event(events) -> tp.Generator[tuple]:
    while events:
        idx: int = rd.randint(0, (len(events) - 1))
        yield events.pop(idx)
    

def main() -> None:
    stream = get_event()
    for c in range(1000):
        name, action = next(stream)
        print(f"Event {c}: Player {name} did action {action}")
    list_events: list = []
    for i in range(10):
        list_events.append(next(stream))
    print(f"Built list of 10 events: {list_events}")
    for event in consume_event(list_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
