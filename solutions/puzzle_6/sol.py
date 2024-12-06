
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"

OBSTACLE = "#"
STARTING_POINT = "^"


def read_data(path: Path) -> list[list[str]]:
    with open(path) as file:
        data = file.read().splitlines()
    return data


def locator(data) -> tuple[tuple, dict, dict]:
    row_obstacles = defaultdict(set)
    col_obstacles = defaultdict(set)
    starting_coordinates = None
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == STARTING_POINT:
                starting_coordinates = row, col
            if data[row][col] == OBSTACLE:
                row_obstacles[row].add(col)
                col_obstacles[col].add(row)
    
    return starting_coordinates, row_obstacles, col_obstacles


def route_guard(data) -> int:
    up = True
    right = False
    left = False
    down = False

    
    starting_coordinates, row_obstacles, col_obstacles = locator(data)
    x, y = starting_coordinates
    visited: set[tuple] = set()
    visited.add(starting_coordinates)
    while True:

        if x == 0 or y == 0 or x == (len(data) - 1) or y == (len(data[0]) - 1):
            break
        if up:
            if data[x-1][y] != OBSTACLE:
                x -= 1
                visited.add((x, y))
            else:
                up = False
                right = True
        elif down:
            if data[x+1][y] != OBSTACLE:
                x += 1
                visited.add((x, y))
            else:
                down = False
                left = True
        elif right:
            if data[x][y+1] != OBSTACLE:
                y += 1
                visited.add((x, y))
            else:
                right = False
                down = True
        elif left:
            if data[x][y-1] != OBSTACLE:
                y -= 1
                visited.add((x, y))
            else:
                left = False
                up = True
    return len(visited)


def get_starting_point(data) -> tuple[int, int]:
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == STARTING_POINT:
                return row, col


def route_guard_loop(data) -> int:
    loops = 0
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    x, y = get_starting_point(data)
    for row in range(len(data)):

        for col in range(len(data[row])):

            if data[row][col] in [STARTING_POINT, OBSTACLE]:
                continue

            new_str = list(data[row])
            new_str[col] = OBSTACLE
            data[row] = "".join(new_str)

            visited = set()
            
            direction = 0
            cur_x, cur_y = x, y

            while cur_x in range(len(data)) and cur_y in range(len(data[row])) and (cur_x, cur_y, direction) not in visited:
                visited.add((cur_x, cur_y, direction))

                cur_dir = directions[direction]
                new_x, new_y = cur_x + cur_dir[0], cur_y + cur_dir[1]

                if new_x in range(len(data)) and new_y in range(len(data[row])) and data[new_x][new_y] == OBSTACLE:
                    direction = (direction + 1) % 4
                else:
                    cur_x, cur_y = new_x, new_y
            
            if (cur_x, cur_y, direction) in visited:
                loops += 1
            new_str = list(data[row])
            new_str[col] = "."
            data[row] = "".join(new_str)

    return loops
        

if __name__ == "__main__":
    data = read_data(DATA_PATH)
    print(route_guard(data))
    print(route_guard_loop(data))
