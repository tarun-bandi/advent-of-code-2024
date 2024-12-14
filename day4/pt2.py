def get_input():
    buffer = None
    with open("input.txt", "r") as f:
        buffer = f.readlines()
        print(buffer)

    return buffer

def find_xmas(grid):
    count = 0

    q = []

    for i in range(len (grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "A":
                q.append((i, j))


    print(f"a count {len(q)} {q}")
    while q:
        a, b = q[0]
        q = q[1:]
        print(f"\nChecking A at ({a}, {b})")
        if a - 1 < 0 or b - 1 < 0 or a + 1 >= len(grid) or b +1 >= len(grid[0]):
            print(f"  Skipped - out of bounds")
            continue
        print(f"  Grid around this A:")
        print(f"  {grid[a-1][b-1]} {grid[a-1][b]} {grid[a-1][b+1]}")
        print(f"  {grid[a][b-1]} {grid[a][b]} {grid[a][b+1]}")
        print(f"  {grid[a+1][b-1]} {grid[a+1][b]} {grid[a+1][b+1]}")
        left_diagonal =  ((grid[a-1][b-1] == "M" and grid[a+1][b+1] == "S") or
        (grid[a+1][b+1] == "M" and grid[a-1][b-1] == "S"))
        right_diagonal = ((grid[a-1][b+1] == "M" and grid[a+1][b-1] == "S") or
        (grid[a-1][b+1] == "S" and grid[a+1][b-1] == "M"))

        print(f"  Left diagonal valid: {left_diagonal}")
        print(f"  Right diagonal valid: {right_diagonal}")

        if left_diagonal and right_diagonal:
            print("Foudn a valid")
            count += 1

    return count

print(find_xmas(get_input()))
