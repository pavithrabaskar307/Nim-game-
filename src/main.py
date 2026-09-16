def calculate_nim_sum(piles):
    """Calculate the Nim-sum using XOR."""
    result = 0

    for pile in piles:
        result ^= pile

    return result


def find_best_move(piles):
    """Find an optimal move for a winning Nim position."""
    total = calculate_nim_sum(piles)

    if total == 0:
        return None

    for i, pile in enumerate(piles):
        target = pile ^ total

        if target < pile:
            return i, pile - target

    return None


def main():
    piles = [3, 4, 5]

    print("===== Nim Game AI =====")
    print("Initial piles:", piles)

    nim_sum = calculate_nim_sum(piles)
    print("Nim-sum:", nim_sum)

    move = find_best_move(piles)

    if move:
        pile_index, objects_removed = move

        print("AI selects pile:", pile_index + 1)
        print("Objects removed:", objects_removed)
        print("Optimal move found!")
    else:
        print("This is a losing position under perfect play.")


if __name__ == "__main__":
    main()
