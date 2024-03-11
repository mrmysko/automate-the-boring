def printTable(some_list: list):

    for key_x, x in enumerate(some_list[0]):
        print()
        for key_y, y in enumerate(some_list):
            print(f"{some_list[key_y][key_x].ljust(10)}", end="")


def main():

    tableData = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]

    printTable(tableData)


if __name__ == "__main__":
    main()
