input = """
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


def get_points_between_two_points_in_straight_line(
    start: tuple[int, int], end: tuple[int, int]
):
    points = [start]
    if start[0] == end[0]:
        for i in range(start[1], end[1]):
            points.append((start[0], i))
    elif start[1] == end[1]:
        for i in range(start[0], end[0]):
            points.append((i, start[1]))
    else:
        if start[0] < end[0] and start[1] < end[1]:
            for i in range(1, end[0] - start[0] + 1):
                points.append((start[0] + i, start[1] + i))
        elif start[0] < end[0] and start[1] > end[1]:
            for i in range(1, end[0] - start[0] + 1):
                points.append((start[0] + i, start[1] - i))
        elif start[0] > end[0] and start[1] < end[1]:
            for i in range(1, start[0] - end[0] + 1):
                points.append((start[0] - i, start[1] + i))
        else:
            for i in range(1, start[0] - end[0] + 1):
                points.append((start[0] - i, start[1] - i))
    return points


def check_potential_locations(
    current_position: tuple[int, int], list_size: tuple[int, int]
):
    potential_locations = []
    if current_position[0] - 3 >= 0:
        potential_locations.append((current_position[0] - 3, current_position[1]))  # Up
        if current_position[1] - 3 >= 0:
            potential_locations.append(
                (current_position[0] - 3, current_position[1] - 3)
            )  # Up-Left
        if current_position[1] + 3 < list_size[1]:
            potential_locations.append(
                (current_position[0] - 3, current_position[1] + 3)
            )  # Up-Right
    if current_position[0] + 3 < list_size[0]:
        potential_locations.append(
            (current_position[0] + 3, current_position[1])
        )  # Down
        if current_position[1] - 3 >= 0:
            potential_locations.append(
                (current_position[0] + 3, current_position[1] - 3)
            )  # Down-Left
        if current_position[1] + 4 < list_size[1]:
            potential_locations.append(
                (current_position[0] + 3, current_position[1] + 3)
            )  # Down-Right
    if current_position[1] - 3 >= 0:
        potential_locations.append(
            (current_position[0], current_position[1] - 3)
        )  # Left
    if current_position[1] + 3 < list_size[1]:
        potential_locations.append(
            (current_position[0], current_position[1] + 3)
        )  # Right
    return potential_locations


def check_for_xmas(
    current_position: tuple[int, int],
    ending_position: tuple[int, int],
    input: list[list[str]],
):
    points_between = get_points_between_two_points_in_straight_line(
        current_position, ending_position
    )
    word = ""
    for point in points_between:
        word += input[point[0]][point[1]]
    return word == "XMAS"


if __name__ == "__main__":
    xmas_count = 0
    split_input = [list(i) for i in input.split("\n") if i != ""]
    for i in range(len(split_input)):
        for j in range(len(split_input[i])):
            if split_input[i][j] == "X":
                current_position = (i, j)
                potential_locations = check_potential_locations(
                    current_position, (len(split_input), len(split_input[0]))
                )
                for location in potential_locations:
                    if check_for_xmas(current_position, location, split_input):
                        xmas_count += 1
    print(xmas_count)
