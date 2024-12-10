test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (1, 1),
    "down_left": (1, -1),
    "down_right": (-1, 1),
}


def parse_input(input: list[str]) -> dict[tuple[int, int], str]:
    return {
        (x, y): input[y][x] for y in range(len(input)) for x in range(len(input[y]))
    }


def word_check(
    word: str,
    letter_map: dict[tuple[int, int], str],
    starting_position: tuple[int, int],
) -> int:
    matches_found = 0
    for direction in directions.values():
        word_okay = True
        x, y = starting_position
        for i in range(len(word)):
            checked_postion = x + direction[0] * i, y + direction[1] * i
            if (
                checked_postion not in letter_map
                or letter_map[checked_postion] != word[i]
            ):
                word_okay = False
        matches_found += word_okay

    return matches_found


if __name__ == "__main__":
    with open("day4/day4.txt") as f:
        # letter_map = parse_input(test_input.strip().split("\n"))
        letter_map = parse_input(f.read().strip().split("\n"))
        positions_with_letter_x = [
            (x, y) for (x, y), letter in letter_map.items() if letter == "X"
        ]
        print(
            "Part 1 answer: ",
            sum(
                [word_check("XMAS", letter_map, pos) for pos in positions_with_letter_x]
            ),
        )
