def digits(n):
    if n >= 0 and n < 10:
        return 1
    elif n >= 10 and n < 100:
        return 2
    elif n >= 100 and n < 1000:
        return 3


def concatenate(x, y):
    return x * 10 ** digits(y) + y


def is_equation_possible(
    numbers, expected_result, current_result=0, with_concatenation=False
):
    if current_result > expected_result:
        return False
    if len(numbers) == 0:
        return expected_result == current_result
    addition = current_result + numbers[0]
    multiplification = current_result * numbers[0]
    concatenation = concatenate(current_result, numbers[0]) if with_concatenation else 0
    if (
        addition > expected_result
        and multiplification > expected_result
        and (not with_concatenation or concatenation > expected_result)
    ):
        return False
    valid = False
    if with_concatenation:
        valid = is_equation_possible(
            numbers[1:],
            expected_result,
            concatenation,
            with_concatenation,
        )
    valid = valid or (
        is_equation_possible(numbers[1:], expected_result, addition, with_concatenation)
        or is_equation_possible(
            numbers[1:], expected_result, multiplification, with_concatenation
        )
    )
    return valid


if __name__ == "__main__":
    valid_equations = []
    for line in open("day7.txt"):
        split_equation = line.split(":")
        result = int(split_equation[0])
        numbers = [int(x) for x in split_equation[1].strip().split(" ")]
        if is_equation_possible(numbers[1:], result, numbers[0], True):
            valid_equations.append(result)
    print(sum(valid_equations))
