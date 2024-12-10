directions = ["^", ">", "v", "<"]

test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def turn_right(direction: int):
    return (direction + 1) % 4


def move(position: tuple[int, int], direction: int):
    x, y = position
    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    elif direction == 3:
        y -= 1
    return x, y


def loop_check(collisions: list[dict], position: tuple[int, int], direction: int):
    for collision in collisions:
        if collision["position"] == position and collision["direction"] == direction:
            return True
    return False


def gaming(map: list[list[str]], position: tuple[int, int], direction: int):
    obstacle_collisions = []
    is_game_over = False
    while not is_game_over:
        current_y, current_x = position
        new_y, new_x = move(position, direction)
        if new_y >= len(map) or new_y < 0 or new_x >= len(map[0]) or new_x < 0:
            print("Game over")
            map[current_y][current_x] = "X"
            return 0
        if map[new_y][new_x] == "#":
            if loop_check(obstacle_collisions, (new_y, new_x), direction):
                print("Loop detected")
                map[current_y][current_x] = "X"
                return 1
            obstacle_collisions.append(
                {
                    "position": (new_y, new_x),
                    "direction": direction,
                }
            )
            direction = turn_right(direction)
        else:
            position = new_y, new_x
            map[new_y][new_x] = directions[direction]
            map[current_y][current_x] = "X"


def find_starting_position(map: list[list[str]]):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return i, j
    return -1, -1


def count_visited_places(map: list[list[str]]):
    count = 0
    for row in map:
        for cell in row:
            if cell == "X":
                count += 1
    return count


def find_visited_places(map: list[list[str]]):
    visited_places = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "X":
                visited_places.append((i, j))
    return visited_places


if __name__ == "__main__":
    looped_variants = 0
    with open("day6.txt") as f:
        map = [list(line.strip()) for line in f]
        # map = [list(line.strip()) for line in test_input.strip().split("\n")]
        map_copy = [row.copy() for row in map]
        starting_position = find_starting_position(map)
        gaming(map_copy, starting_position, 0)
        print(count_visited_places(map_copy))
        for place in find_visited_places(map_copy):
            map_copy_part_2 = [row.copy() for row in map]
            map_copy_part_2[place[0]][place[1]] = "#"
            if gaming(map_copy_part_2, starting_position, 0) == 1:
                looped_variants += 1
        print(looped_variants)
