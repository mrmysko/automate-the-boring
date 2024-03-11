def comma_code(lst: list) -> str:

    return ", ".join(lst)


if __name__ == "__main__":
    print(comma_code(["apples", "bananas", "tofu", "cats"]))
    print(comma_code([]))
