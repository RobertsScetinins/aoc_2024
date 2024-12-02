
import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "aoc_1.csv"


def read_data(path: Path) -> tuple[list]:
    left_list = []
    right_list = []
    with open(path) as file:
        csv_file = csv.reader(file, delimiter=" ")
        for row in csv_file:
            left_list.append(int(row[0]))
            right_list.append(int(row[1]))
    return left_list, right_list


def calculate_distances(left_list: list[int], right_list: list[int]) -> int:
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total = 0
    for i in zip(left_sorted, right_sorted):
        total += abs(i[0] - i[1])
    print(total)
    return total


def calculate_similarities(left_list: list[int], right_list: list[int]) -> int:
    total = 0
    counter: dict[int, int] = {}
    for i in left_list:
        if i not in counter:
            count = right_list.count(i)
            counter[i] = count
        total += counter[i] * i

    print(total)
    return total


if __name__ == "__main__":
    left_list, right_list = read_data(DATA_PATH)
    calculate_distances(left_list, right_list)
    calculate_similarities(left_list, right_list)