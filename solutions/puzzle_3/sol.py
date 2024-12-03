
from pathlib import Path
import re

DATA_PATH = Path(__file__).parent / "data.txt"

REGEX = r"mul\((\d+)\,(\d+)\)"
REGEX_OPTIONAL = r"(do\(\)|don't\(\)|mul(\((\d+)\,(\d+)\)))"


def read_data(path: Path) -> tuple[list]:
    with open(path) as file:
        data = file.readline()
    return data


def multiply(data) -> int:
    r = re.findall(REGEX, data)
    result = 0
    for x, y in r:
        result += int(x) * int(y)
    return result


def multiply_optional(data) -> int:
    r = re.findall(REGEX_OPTIONAL, data)
    result = 0
    mul_enabled = True

    for i in r:
        if i[0] == "do()":
            mul_enabled = True
        elif i[0] == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                result += int(i[2]) * int(i[3])
    return result


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    res = multiply(data)
    print(res)
    res = multiply_optional(data)
    print(res)
