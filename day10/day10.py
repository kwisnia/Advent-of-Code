test_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def move(
    map: list[list[int]],
    position: tuple[int, int],
    previous_position: tuple[int, int] = None,
    node_history: list[str, dict[str, tuple[int, int] | int]] = None,
):
    current_y, current_x = position
    level = map[current_y][current_x]
    if node_history is None:
        node_history = [
            {
                "position": position,
                "level": level,
            }
        ]

    potential_moves = []
    if current_y - 1 >= 0:
        potential_moves.append((current_y - 1, current_x))
    if current_y + 1 < len(map):
        potential_moves.append((current_y + 1, current_x))
    if current_x - 1 >= 0:
        potential_moves.append((current_y, current_x - 1))
    if current_x + 1 < len(map[0]):
        potential_moves.append((current_y, current_x + 1))
    if previous_position is not None:
        potential_moves.remove(previous_position)
    for potential_move in potential_moves:
        y, x = potential_move
        if map[y][x] == level + 1:
            node = {
                "level": level + 1,
                "position": potential_move,
            }
            node_history.append(node)
            if level + 1 < 9:
                move(map, potential_move, position, node_history)

    return node_history


def calculate_level_9_nodes(
    places: list[dict[str, tuple[int, int] | int]],
    count_not_unique_paths: bool = False,
):
    if count_not_unique_paths:
        return len([node for node in places if node["level"] == 9])
    else:
        level_9_unique_positions = {
            node["position"] for node in places if node["level"] == 9
        }
        return len(level_9_unique_positions)


def print_tree(tree: list[dict]):
    for node in tree:
        print(node)


def find_starting_positions(map: list[list[int]]):
    starting_positions = []
    for y, row in enumerate(map):
        for x, level in enumerate(row):
            if level == 0:
                starting_positions.append((y, x))
    return starting_positions


if __name__ == "__main__":
    with open("day10/day10.txt") as f:
        # map = [
        #     [int(x) for x in line.strip()] for line in test_input.strip().split("\n")
        # ]
        map = [[int(x) for x in line.strip()] for line in f]
        starting_positions = find_starting_positions(map)
        possible_paths = [move(map, position) for position in starting_positions]
        print(
            "Part 1 answer:",
            sum(
                [
                    calculate_level_9_nodes(path, count_not_unique_paths=False)
                    for path in possible_paths
                ]
            ),
        )
        print(
            "Part 2 answer:",
            sum(
                [
                    calculate_level_9_nodes(path, count_not_unique_paths=True)
                    for path in possible_paths
                ]
            ),
        )
