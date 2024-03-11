import random


def main(iterations: int):
    flips = list()
    streak = 0

    for i in range(iterations):
        flips.append(coin_flip())

    # This doesnt work, it counts a 7 strak as 2 separate streaks. I need to increment the iterator manually somehow.
    # for index in flips:
    index = 0
    while index < len(flips):
        if index + 6 < len(flips):
            if (
                "H" not in flips[index : index + 6]
                or "T" not in flips[index : index + 6]
            ):
                # Move index past the streak.
                flips.insert(index, "Streak ->")
                index += 7
                # Increment streak.
                streak += 1
        index += 1

    print("Change of streak over %s iterations: %s%%" % (iterations, streak / 100))


def coin_flip():
    coins = ["H", "T"]

    return random.choice(coins)


if __name__ == "__main__":
    main(100_000)
