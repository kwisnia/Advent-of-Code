test_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def get_antenna_map(antenna_map_str: list[str]) -> dict[tuple[int, int], str]:
    antenna_map = {}
    for y, line in enumerate(antenna_map_str):
        for x, char in enumerate(line):
            if char != ".":
                antenna_map[(x, y)] = char
    return antenna_map


def place_antinodes(
    antennas: tuple[tuple[int, int], tuple[int, int]],
    antenna_frequency: str,
    map_size: tuple[int, int],
    antinode_list: dict[tuple[int, int], list[str]],
) -> None:
    first_antenna, second_antenna = antennas
    location_vector = (
        first_antenna[0] - second_antenna[0],
        first_antenna[1] - second_antenna[1],
    )
    antinode_location = (
        first_antenna[0] + location_vector[0],
        first_antenna[1] + location_vector[1],
    )
    antinode_x, antinode_y = antinode_location
    if (
        antinode_x < map_size[0]
        and antinode_x >= 0
        and antinode_y < map_size[1]
        and antinode_y >= 0
    ):
        if antinode_location not in antinode_list:
            antinode_list[antinode_location] = [antenna_frequency]
        else:
            antinode_list[antinode_location].append(antenna_frequency)


if __name__ == "__main__":
    with open("day8/day8.txt") as f:
        # split_input = test_input.strip().split("\n")
        split_input = f.read().strip().split("\n")
        map_size = (len(split_input)), len(split_input[0])
        antenna_map = get_antenna_map(split_input)
        print(antenna_map)
        antinode_list = {}
        for antennas, frequency in antenna_map.items():
            for antennas_2, frequency_2 in antenna_map.items():
                if antennas != antennas_2 and frequency == frequency_2:
                    place_antinodes(
                        (antennas, antennas_2), frequency, map_size, antinode_list
                    )
        # print(antinode_list)
        print(len(antinode_list))