import random as rd


class Player:
    def __init__(self, name: str, achievements: set):
        self.name = name
        self.achievements = set(achievements)

    def __str__(self):
        return f"Player {self.name}: {self.achievements}"

    def print_unique(self, others: set):
        unique = self.achievements.difference(others)
        print(f"Only {self.name} has: {unique}")

    def print_missing(self, all_achievements: set):
        missing = all_achievements.difference(self.achievements)
        print(f"{self.name} is missing: {missing}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achievements = [
        'Speed Demon', 'Shadow Walker', 'Treasure Hunter',
        'Pacifist Run', 'Master Chef', 'Pixel Perfect',
        'Lone Wolf', 'Jack of All Trades', 'Money Maker',
        'Time Traveler', 'Sharpshooter', 'Survivor', 'Architect',
        'Alchemist', 'Legendary Hero', 'Dungeon Master',
        'Grandmaster', 'Master Thief', 'Iron Will', 'Berserker',
        'Cartographer', 'Bounty Hunter', 'Lore Master',
        'Gladiator', 'Necromancer', 'Titan Slayer', 'Untouchable',
        'Speedrunner', 'Omniscient', 'True Ending'
    ]

    player_alice = Player("Alice", set(rd.sample(achievements, k=11)))
    player_bob = Player("Bob", set(rd.sample(achievements, k=10)))
    player_charlie = Player("Charlie", set(rd.sample(achievements, k=12)))
    player_dylan = Player("Dylan", set(rd.sample(achievements, k=8)))

    all_distinct = set.union(
        player_dylan.achievements,
        player_charlie.achievements,
        player_bob.achievements,
        player_alice.achievements
    )

    common_achievements = (
        player_dylan.achievements
        & player_charlie.achievements
        & player_bob.achievements
        & player_alice.achievements
    )

    print(player_alice)
    print(player_bob)
    print(player_charlie)
    print(player_dylan)
    print()

    print(f"All distinct: {all_distinct}\n")
    print(f"Common achievements: {common_achievements}\n")

    player_alice.print_unique(
        set.union(
            player_dylan.achievements,
            player_charlie.achievements,
            player_bob.achievements
        )
    )

    player_bob.print_unique(
        set.union(
            player_dylan.achievements,
            player_charlie.achievements,
            player_alice.achievements
        )
    )

    player_charlie.print_unique(
        set.union(
            player_dylan.achievements,
            player_bob.achievements,
            player_alice.achievements
        )
    )

    player_dylan.print_unique(
        set.union(
            player_charlie.achievements,
            player_bob.achievements,
            player_alice.achievements
        )
    )

    print()

    player_alice.print_missing(
        set.union(
            player_dylan.achievements,
            player_charlie.achievements,
            player_bob.achievements
        )
    )

    player_bob.print_missing(
        set.union(
            player_dylan.achievements,
            player_charlie.achievements,
            player_alice.achievements
        )
    )

    player_charlie.print_missing(
        set.union(
            player_dylan.achievements,
            player_bob.achievements,
            player_alice.achievements
        )
    )

    player_dylan.print_missing(
        set.union(
            player_charlie.achievements,
            player_bob.achievements,
            player_alice.achievements
        )
    )


if __name__ == "__main__":
    main()
