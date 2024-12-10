import re


test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

mul_regex = re.compile(r"mul\(\d\d?\d?,\d\d?\d?\)")

part_2_regex = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")


def multiply(x: int, y: int):
    return x * y


if __name__ == "__main__":
    with open("day3/day3.txt") as f:
        input = f.read()
        # Part 1
        mul_matches = mul_regex.findall(input)
        mul_sum = 0
        for match in mul_matches:
            match_digits = re.findall(r"\d\d?\d?", match)
            x, y = int(match_digits[0]), int(match_digits[1])
            mul_sum += multiply(x, y)
        print("Part 1 solution: ", mul_sum)
        # Part 2
        mul_enabled = True
        part_2_matches = part_2_regex.findall(input)
        part_2_sum = 0
        for match in part_2_matches:
            if match == "do()":
                mul_enabled = True
            elif match == "don't()":
                mul_enabled = False
            else:
                if mul_enabled:
                    match_digits = re.findall(r"\d{1,3}", match)
                    x, y = int(match_digits[0]), int(match_digits[1])
                    part_2_sum += multiply(x, y)
        print("Part 2 solution: ", part_2_sum)
