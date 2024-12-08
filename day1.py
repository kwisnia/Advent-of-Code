import csv


def read_data(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def part1(data):
    sum_of_distances = 0
    sorted_first_list = sorted([int(i[0]) for i in data])
    sorted_second_list = sorted([int(i[1]) for i in data])
    for i, j in zip(sorted_first_list, sorted_second_list):
        sum_of_distances += abs(i - j)
    return sum_of_distances


def part2(data):
    similiarity_score = 0
    first_list = [int(i[0]) for i in data]
    second_list = [int(i[1]) for i in data]
    for i in first_list:
        similiarity_score += i * second_list.count(i)
    return similiarity_score


if __name__ == "__main__":
    sum_of_distances = 0
    data = read_data("day1.csv")
    sum_of_distances = part1(data)
    print(sum_of_distances)
    similiarity_score = part2(data)
    print(similiarity_score)
