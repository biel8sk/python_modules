import math as m


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            raw = input("Enter new coordinates as float in format 'x,y,z': ")
            if (not raw.__contains__(',') or len(raw.split(',')) != 3):
                print("Invalid syntax")
                continue
            sx, sy, sz = [p.strip() for p in raw.split(',')]
            (x, y, z) = float(sx), float(sy), float(sz)
            return (x, y, z)
        except Exception as ex:
            print(f"Error: {ex}")
            continue


def calc_distance(t: tuple, t2: None):
    if t2 == None: return (m.sqrt((t[0]**2)+(t[1]**2)+(t[2]**2)))
    return (m.sqrt(((t2[0]-t[0])**2)+((t2[1]-t[1])**2)+((t2[2]-t[2])**2)))


def main() -> None:
    print("=== Game Coordinate System ===\n\n"
            "Get a first set of coordinates")
    result = get_player_pos()
    print(f"Got a first tuple: {result}")
    print(f"It includes: X={result[0]} Y={result[1]} Z={result[2]}")
    print(f"Distance to center: {calc_distance(result, None):.4f}\n")
    print(f"Get a second set of coordinates")
    result2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{calc_distance(result, result2):.4f}")
    

if __name__ == "__main__":
    main()
