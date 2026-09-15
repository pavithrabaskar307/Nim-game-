def nim_sum(piles):
    result = 0
    for pile in piles:
        result ^= pile
    return result


def find_best_move(piles):
    total = nim_sum(piles)

    if total == 0:
        return None

    for i, pile in enumerate(piles):
        target = pile ^ total

        if target < pile:
            return i, pile - target

    return None


def main():
    piles = [3, 4, 5]

    print("Welcome to Nim Game AI")
    print("Initial piles:", piles)

    total = nim_sum(piles)
    print("Nim-sum:", total)

    move = find_best_move(piles)

    if move:
        index, remove = move
        print("AI removes", remove,
              "objects from pile", index + 1)
        print("Optimal move found!")
    else:
        print("This is a losing position under perfect play.")


if __name__ == "__main__":
    main()
