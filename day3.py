import re


test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

mul_regex = re.compile(r"mul\(\d\d?\d?,\d\d?\d?\)")


def multiply(x: int, y: int):
    return x * y


if __name__ == "__main__":
    with open("day3.txt") as f:
        input = f.read()
        mul_matches = mul_regex.findall(input)
        mul_sum = 0
        for match in mul_matches:
            match_digits = re.findall(r"\d\d?\d?", match)
            x, y = int(match_digits[0]), int(match_digits[1])
            mul_sum += multiply(x, y)
        print(mul_sum)
