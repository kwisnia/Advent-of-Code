from itertools import islice

test_input = "2333133121414131402"


def calculate_disk(input: str):
    disk_map = []
    free_space_lookup = []
    file_index = 0
    disk_length = 0
    for i in range(0, len(input), 2):
        number = int(input[i])
        disk_length += number
        for _ in range(number):
            disk_map.append(file_index)
        file_index += 1
        if i + 1 < len(input):
            free_spaces = int(input[i + 1])
            free_space_lookup.append(
                {"starting_index": disk_length, "free_spaces": free_spaces}
            )
            disk_length += free_spaces
            for _ in range(free_spaces):
                disk_map.append(None)
    return disk_map, free_space_lookup


def calculate_disk_lookups(input: str):
    disk_lookup = {}
    free_space_lookup = []
    file_index = 0
    disk_length = 0
    for i in range(0, len(input), 2):
        number = int(input[i])
        disk_lookup[disk_length] = {"file_index": file_index, "length": number}
        file_index += 1
        disk_length += number
        if i + 1 < len(input):
            free_spaces = int(input[i + 1])
            if free_spaces > 0:
                free_space_lookup.append((disk_length, free_spaces))
                disk_length += free_spaces

    return disk_lookup, free_space_lookup


def move_file_parts_to_leftmost_free_spaces(disk_map: list[int]):  # Part 1
    j = len(disk_map) - 1
    for i in range(len(disk_map)):
        if i >= j:
            break
        if disk_map[i] is None:
            while disk_map[j] is None:
                j -= 1
            disk_map[i] = disk_map[j]
            disk_map[j] = None
    disk_map.remove(None)
    disk_map.append(None)
    return disk_map


def move_files_to_left_lookup(
    disk_map: list[int], lookup: list[dict[str, int]]
):  # Working
    last_file_index = disk_map[len(disk_map) - 1]
    last_file_length = 0
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] == last_file_index:
            last_file_length += 1
        elif last_file_length > 0:
            for j in range(0, len(lookup)):
                if (
                    lookup[j]["free_spaces"] >= last_file_length
                    and lookup[j]["starting_index"] <= i
                ):
                    for k in range(0, last_file_length):
                        disk_map[lookup[j]["starting_index"] + k] = disk_map[i + k + 1]
                        disk_map[i + k + 1] = None
                    lookup[j]["free_spaces"] -= last_file_length
                    lookup[j]["starting_index"] += last_file_length
                    break
            last_file_length = 0
            last_file_index -= 1
            if disk_map[i] == last_file_index:
                last_file_length += 1
    return disk_map


def move_files_to_left_double_lookup(
    disk_lookup: dict[int, int], free_lookup: list[tuple[int, int]]
):
    for file_position, file_info in reversed(disk_lookup.copy().items()):
        file_length = file_info["length"]
        for i in range(len(free_lookup)):
            free_position, free_length = free_lookup[i]
            if free_length >= file_length and free_position < file_position:
                disk_lookup[free_position] = file_info
                disk_lookup.pop(file_position)
                if free_length == file_length:
                    free_lookup.pop(i)
                else:
                    free_lookup[i] = (
                        free_position + file_length,
                        free_length - file_length,
                    )
                break
    return disk_lookup


def calculate_checksum(disk_map: list[int]):
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] is not None:
            checksum += i * disk_map[i]
    return checksum


def calculate_checksum_lookup(disk_lookup: dict[str, int]):
    checksum = 0
    for key, value in disk_lookup.items():
        for i in range(key, key + value["length"]):
            checksum += i * value["file_index"]
    return checksum


if __name__ == "__main__":
    with open("day9.txt") as f:
        input = f.read().strip()
        disk_lookup, free_lookup = calculate_disk_lookups(input)
        disk_lookup = move_files_to_left_double_lookup(disk_lookup, free_lookup)
        check_sum = calculate_checksum_lookup(disk_lookup)
        print(check_sum)
