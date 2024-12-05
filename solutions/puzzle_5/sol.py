
from collections import defaultdict
from pathlib import Path

RULE_PATH = Path(__file__).parent / "rules.txt"
DATA_PATH = Path(__file__).parent / "data.txt"


def read_data(path: Path) -> list[list[str]]:
    with open(path) as file:
        data = file.read().splitlines()
    return data


def check_sort(row, rules_map):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[j] not in rules_map[row[i]]:
                return False
    return True


def fix_sorting(row: list[str], rules_map: dict):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[j] not in rules_map[row[i]]:
                row.insert(i, row.pop(j))
    return row


def parse_data(rules: dict[set], data: list[str]):
    count = 0
    for row in data:
        if check_sort(row, rules):
            count += int(row[len(row) // 2])
    return count


def parse_data_fixed(rules, data: list[str]):
    count = 0
    for row in data:
        if not check_sort(row, rules):
            row = fix_sorting(row, rules)
            count += int(row[len(row) // 2])
    return count
                        

if __name__ == "__main__":
    rules = read_data(RULE_PATH)
    rules_map = defaultdict(set)
    for rule in rules:
        i = rule.split("|")
        rules_map[i[0]].add(i[1])

    data = read_data(DATA_PATH)
    data = [i.split(",") for i in data]
    print(parse_data(rules_map, data))
    print(parse_data_fixed(rules_map, data))
