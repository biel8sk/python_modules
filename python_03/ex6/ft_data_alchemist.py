import random as rd


def main():
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
    'john', 'kevin', 'Liam']
    print(f"Inital list of players: {initial_list}")
    all_captlz = [x.capitalize() for x in initial_list]
    captlz_only = [x for x in initial_list if x.capitalize() == x]
    dic_score = {name: rd.randint(0, 1000) for name in initial_list}
    average = sum(dic_score.values()) / len(dic_score.values())
    high_scores = {x for x in dic_score.items() if x[1] > average}
    print(f"New list of all capitalized: {all_captlz}")
    print(f"New list of capilized only: {captlz_only}\n")
    print(f"Score dict: {dic_score}")
    print(f"Score avarege is {average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    main()
