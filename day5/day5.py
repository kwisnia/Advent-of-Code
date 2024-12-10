test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def prepare_ruleset(input: str) -> set[tuple[int, int]]:
    return {tuple(map(int, line.split("|"))) for line in input.strip().split("\n")}


def check_line(line: list[int], ruleset: set[tuple[int, int]]) -> bool:
    for i in range(1, len(line)):
        for j in range(i - 1, -1, -1):
            if (line[i], line[j]) in ruleset:
                return False
    return True


def fix_order(line: list[int], ruleset: set[tuple[int, int]]) -> list[int]:
    while True:
        correct = True
        for i in range(1, len(line)):
            for j in range(i - 1, -1, -1):
                if (line[i], line[j]) in ruleset:
                    correct = False
                    line.insert(j, line.pop(i))
                    break
            if not correct:
                break
        if correct:
            return line


if __name__ == "__main__":
    with open("day5/day5.txt") as f:
        ruleset_input, task_input = f.read().split("\n\n")
        # ruleset_input, task_input = test_input.split("\n\n")
        ruleset = prepare_ruleset(ruleset_input.strip())
        sum_of_middle = 0
        invalid_lines = []
        for line_str in task_input.strip().split("\n"):
            line = [int(x) for x in line_str.split(",")]
            if check_line(line, ruleset):
                sum_of_middle += line[len(line) // 2]
            else:
                invalid_lines.append(line)
        print("Part 1 answer:", sum_of_middle)
        sum_of_middle = 0
        for line in invalid_lines:
            fixed_line = fix_order(line, ruleset)
            sum_of_middle += fixed_line[len(fixed_line) // 2]
        print("Part 2 answer:", sum_of_middle)
