import sys


def extract_scores(args):
    numbers: list[int] = []
    for arg in args:
        try:
            numbers.append(int(arg))
        except Exception:
            print(f"Invalid parameter: {arg}")
    return numbers


def main():
    args = sys.argv
    print("=== Player Score Analytics ===")
    if (len(args) < 2):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
        return
    scores = extract_scores(args[1:])
    if (len(scores) < 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
        return
    average = sum(scores) / len(scores)
    score_min = min(scores)
    score_max = max(scores)
    score_range = score_max - score_min
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Average score: {average}")
    print(f"Highest: {score_max}")
    print(f"Lowest: {score_min}")
    print(f"Score range: {score_range}")
    print()


if __name__ == "__main__":
    main()
