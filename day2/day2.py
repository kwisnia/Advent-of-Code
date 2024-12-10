def is_decending(x, y):
    return x > y


def is_ascending(x, y):
    return x < y


def check_line(numbers: list[int], dampen: bool = False):
    valid = True
    continuity_func = is_decending if numbers[0] > numbers[1] else is_ascending
    if dampen:
        valid = check_line(numbers[1:], False)
        if valid:
            return True
    for i in range(1, len(numbers)):
        if not (
            abs(numbers[i - 1] - numbers[i]) >= 1
            and abs(numbers[i - 1] - numbers[i]) <= 3
        ) or not continuity_func(numbers[i - 1], numbers[i]):
            if not dampen:
                valid = False
                break
            numbers.pop(i)
            valid = check_line(numbers, False)
            break

    return valid


if __name__ == "__main__":
    valid_reports = 0
    for line in open("day2.txt"):
        valid = check_line([int(x) for x in line.strip().split(" ")], True)
        if valid:
            valid_reports += 1
    print(valid_reports)
