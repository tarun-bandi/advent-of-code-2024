

def get_input():
    buffer = None
    with open("input.txt", "r") as f:
        buffer = f.readlines()

    return buffer

def find_xmas(grid):
    count = 0

    q = []

    for i in range(len (grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                q.append((i, j))

    while q:
        a, b = q.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1),
                       (-1, 1), (1, -1)]:
            x, y = a, b
            xmas = "XMAS"
            holds = True
            for i in range(4):
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and xmas[i] == grid[x][y]:
                    x += dx
                    y += dy
                else:
                    holds = False
                    break

            x -= dx
            y -= dy
            if holds:
                print(f"Holds at {x} and {y} {grid[x][y]} direction {dx, dy}")
                count += 1

    print(f"count {count}")


    return count

find_xmas(get_input())
