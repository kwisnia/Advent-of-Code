test_input = "125 17"


def digits(n: int) -> int:
    result = 0
    while n > 0:
        result += 1
        n = n // 10
    return result


def split_number_into_two(n: int, digits: int) -> tuple[int, int]:
    return n // 10 ** (digits // 2), n % 10 ** (digits // 2)


def blink(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        digits_count = digits(number)
        if number == 0:
            result.append(1)
        elif digits_count % 2 == 0:
            result.extend(split_number_into_two(number, digits_count))
        else:
            result.append(number * 2024)
    return result


if __name__ == "__main__":
    with open("day11/day11.txt") as f:
        split_input = f.read().strip().split(" ")
        # split_input = test_input.strip().split(" ")
        numbers = [int(x) for x in split_input]
        for _ in range(25):
            numbers = blink(numbers)
        print(len(numbers))
