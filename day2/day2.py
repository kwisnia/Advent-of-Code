def is_decending(x, y):
    return x > y


def is_ascending(x, y):
    return x < y


def check_line(numbers: list[int], dampen: bool = False):
    valid = True
    continuity_func = is_decending if numbers[0] > numbers[1] else is_ascending
    for i in range(0, len(numbers) - 1):
        if not (
            abs(numbers[i] - numbers[i + 1]) >= 1
            and abs(numbers[i] - numbers[i + 1]) <= 3
        ) or not continuity_func(numbers[i], numbers[i + 1]):
            if not dampen:
                valid = False
                break
            for j in range(0, len(numbers)):
                if check_line(numbers[:j] + numbers[j + 1 :], False):
                    return True
            valid = False

    return valid


if __name__ == "__main__":
    valid_reports = 0
    for line in open("day2/day2.txt"):
        valid = check_line([int(x) for x in line.strip().split(" ")], True)
        if valid:
            valid_reports += 1
    print(valid_reports)
    print(
        check_line(
            [3, 6, 4, 2, 1],
            True,
        )
    )
