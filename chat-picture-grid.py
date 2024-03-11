def main():
    grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]

    for key_x, x in enumerate(grid[0]):
        print()
        for key_y, y in enumerate(grid):
            print(grid[key_y][key_x], end="")


if __name__ == "__main__":
    main()
