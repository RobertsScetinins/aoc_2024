

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"


def read_data(path: Path) -> list[list[str]]:
    with open(path) as file:
        data = file.read().splitlines()
    return data


def check_horizontal(row: str) -> int:
    count = 0
    
    # possible_xmas_1 = data[x][y:y+4]
    # possible_xmas_2 = data[x][y-3:y+1]
    # if "XMAS" in possible_xmas_1:
    #     count += 1
    
    # if "SAMX" in possible_xmas_2:
    #     count += 1
    count += row.count("XMAS")
    count += row.count("SAMX")

    return count


def check_diagonal(x, y, data):
    count = 0

    max_row = len(data)
    max_col = len(data[x])

    if x + 3 < max_row and y + 3 < max_col:
        possible_xmas = ""
        for i in range(4):
            possible_xmas += data[x + i][y + i]
        if "XMAS" in possible_xmas:
            count += 1

    if x - 3 >= 0 and y - 3 >= 0:
        possible_xmas = ""
        for i in range(4):
            possible_xmas += data[x - i][y - i]
        if "XMAS" in possible_xmas:
            count += 1

    if x + 3 < max_row and y - 3 >= 0:
        possible_xmas = ""
        for i in range(4):
            possible_xmas += data[x + i][y - i]
        if "XMAS" in possible_xmas:
            count += 1

    if x - 3 >= 0 and y + 3 < max_col:
        possible_xmas = ""
        for i in range(4):
            possible_xmas += data[x - i][y + i]
        if "XMAS" in possible_xmas:
            count += 1

    return count


def check_diagonal_mas(x, y, data):
    count = 0

    max_row = len(data)
    max_col = len(data[x])

    if x + 1 < max_row and y - 1 >= 0 and x - 1 >= 0 and y + 1 < max_col:
        possible_xmas = data[x - 1][y - 1] + data[x][y] + data[x + 1][y + 1]
        if possible_xmas in ["SAM", "MAS"]:
            count += 1

        possible_xmas = data[x + 1][y - 1] + data[x][y] + data[x - 1][y + 1]
        if possible_xmas in ["SAM", "MAS"]:
            count += 1

    if count > 1:
        return True
    return False


def check_vertical(x, y, data) -> int:
    count = 0
    max_row = len(data)

    if x + 3 < max_row:
        possible_xmas_1 = ""
        for i in range(4):
            possible_xmas_1 += data[x + i][y]
        if "XMAS" in possible_xmas_1:
            count += 1

    if x - 3 >= 0:
        possible_xmas_2 = ""
        for i in range(4):
            possible_xmas_2 += data[x - i][y]
        if "XMAS" in possible_xmas_2:
            count += 1
    return count


def find_xmas(data: list[list[str]]) -> int:
    count = 0

    for row in range(len(data)):
        count += check_horizontal(data[row])
        for col in range(len(data[row])):

            if data[row][col] == "X":
                # print(row, col)
                count += check_vertical(row, col, data)
                count += check_diagonal(row, col, data)
    return count


def find_mas(data: list[list[str]]) -> int:
    count = 0

    for row in range(len(data)):
        for col in range(len(data[row])):

            if data[row][col] == "A":
                # print(row, col)
                if check_diagonal_mas(row, col, data):
                    count += 1
    return count


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    count = find_xmas(data)
    print(count)
    count = find_mas(data)
    print(count)
