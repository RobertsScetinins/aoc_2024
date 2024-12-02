
import csv
from pathlib import Path
from typing import Literal

DATA_PATH = Path(__file__).parent / "data.csv"


def read_data(path: Path) -> list[list[int]]:
    data = []
    with open(path) as file:
        csv_file = csv.reader(file, delimiter=" ")
        for row in csv_file:
            row = [int(i) for i in row]
            data.append(row)
    return data


def is_sorted(row: list[int], mode: Literal["asc", "desc"] = "asc") -> bool:
    # TODO: do both in one go
    for i in range(len(row) - 1):
        if mode == "asc":
            diff = row[i+1] - row[i]
        elif mode == "desc":
            diff = row[i] - row[i+1]
        if 1 <= diff <= 3:
            continue
        else:
            return False
    return True


def is_sorted_tolerant(row: list[int], mode: Literal["asc", "desc"] = "asc") -> bool:
    def check_sorted(lst: list[int]) -> bool:
        for i in range(len(lst) - 1):
            if mode == "asc":
                diff = lst[i+1] - lst[i]
            elif mode == "desc":
                diff = lst[i] - lst[i+1]
            if not (1 <= diff <= 3):
                return False
        return True

    if check_sorted(row):
        return True

    for i in range(len(row)):
        modified_row = row[:i] + row[i+1:]
        if check_sorted(modified_row):
            return True


def count_safe_reports(data: list[list[int]]) -> int:
    count = 0
    for row in data:
        if is_sorted(row) or is_sorted(row, "desc"):
            count += 1
    return count


def count_safe_reports_tolerant(data: list[list[int]]) -> int:
    count = 0
    for row in data:
         if is_sorted_tolerant(row) or is_sorted_tolerant(row, "desc"):
            count += 1
    return count


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    count = count_safe_reports(data)
    print(count)
    count_tolerant = count_safe_reports_tolerant(data)
    print(count_tolerant)
