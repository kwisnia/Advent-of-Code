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
    count_not_unique_paths: bool = False,
    previous_position: tuple[int, int] = None,
    current_tree: dict[tuple[int, int], dict[str, tuple[int, int] | int]] = None,
):
    if current_tree is None:
        if count_not_unique_paths:
            current_tree = [
                {
                    "position": position,
                    "parent": None,
                    "level": map[position[0]][position[1]],
                }
            ]
        else:
            current_tree = {
                position: {
                    "parent": None,
                    "level": map[position[0]][position[1]],
                }
            }
    current_y, current_x = position
    level = map[current_y][current_x]
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
                "parent": position,
                "level": level + 1,
            }
            if count_not_unique_paths:
                node["position"] = potential_move
                current_tree.append(node)
                move(
                    map, potential_move, count_not_unique_paths, position, current_tree
                )
            else:
                if potential_move not in current_tree:
                    current_tree[potential_move] = node
                    if level + 1 < 9:
                        move(
                            map,
                            potential_move,
                            count_not_unique_paths,
                            position,
                            current_tree,
                        )

    return current_tree


def calculate_level_9_tree_width(
    tree: dict[tuple[int, int], dict[str, tuple[int, int] | int]]
    | list[dict[str, tuple[int, int] | int]]
):
    if isinstance(tree, list):
        level_9_positions = [node for node in tree if node["level"] == 9]
    else:
        level_9_positions = [
            position for position in tree if tree[position]["level"] == 9
        ]

    return len(level_9_positions)


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
        print(
            "Part 1 answer:",
            sum(
                [
                    calculate_level_9_tree_width(move(map, position))
                    for position in starting_positions
                ]
            ),
        )
        print(
            "Part 2 answer:",
            sum(
                [
                    calculate_level_9_tree_width(
                        move(map, position, count_not_unique_paths=True)
                    )
                    for position in starting_positions
                ]
            ),
        )
