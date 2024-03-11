def main():
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = int(num)
            break

    while collatz(num) != 1:
        num = collatz(num)


def collatz(number: int) -> int:
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


if __name__ == "__main__":
    main()
