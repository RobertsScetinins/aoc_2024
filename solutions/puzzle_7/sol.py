
from itertools import product
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"

OPERATIONS = ["+", "*"]
OPERATIONS_CONCAT = OPERATIONS + ["||"]


def read_data(path: Path) -> list[list[str]]:
    with open(path) as file:
        data = file.read().splitlines()
    return data


def parse_data(data) -> list[tuple[int, list[int]]]:
    parsed_data = []
    for row in data:
        row_split = row.split(":")
        total = int(row_split[0])
        numbers = list(map(int, row_split[1].strip().split(" ")))
        parsed_data.append((total, numbers))
    return parsed_data


def combine(numbers: list[int], operations: list[str]) -> int:
    total = numbers[0]
    for n, operation in enumerate(operations):
        if operation == "+":
            total += numbers[n+1]
        elif operation == "*":
            total *= numbers[n+1]
        elif operation == "||":
            total = int(str(total) + str(numbers[n+1]))
    return total


def solve(data: list[tuple[int, list[int]]], operations: list[str]) -> int:
    total = 0

    for i in data:
        target = i[0]
        numbers = i[1]
        combinations = list(product(operations, repeat=len(numbers)-1))
        for combination in combinations:
            if target == combine(numbers, combination):
                total += target
                break
    return total


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    raw_equations = parse_data(data)
    print(solve(raw_equations, OPERATIONS))
    print(solve(raw_equations, OPERATIONS_CONCAT))
