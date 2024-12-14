import enum
def get_input():

    res = None

    with open("input.txt", "r") as file:
        res = file.readlines()

    return res

class direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def draw_path(graph):
    guard_direction = None
    position = None
    for row in range(len(graph)):
        graph[row] = list(graph[row])
    for row in range(len(graph)):
        for col in range(row):
            #print(position, len(graph), len(graph[0]))
            if graph[row][col] == ">":
                guard_direction = direction.RIGHT
                position = (row, col)
            elif graph[row][col] == "<":
                guard_direction = direction.LEFT
                position = (row, col)
            elif graph[row][col] == "^":
                guard_direction = direction.UP
                position = (row, col)
            elif graph[row][col] == "v":
                guard_direction = direction.DOWN
                position = (row, col)
            elif direction is None:
                position = None
    
    #simulate
    transition = {direction.RIGHT: direction.DOWN, direction.LEFT: direction.UP, direction.UP: direction.RIGHT, direction.DOWN: direction.LEFT}
    cells_seen = set()
    while 0 <= position[0] < len(graph) and 0 <= position[1] < len(graph[0]):
        if graph[position[0]][position[1]] == '#':
            #Undo the previous move:
            if guard_direction == direction.RIGHT:
                position = (position[0], position[1] - 1)
            elif guard_direction == direction.LEFT:
                position = (position[0], position[1] + 1)
            elif guard_direction == direction.UP:
                position = (position[0] + 1, position[1])
            elif guard_direction == direction.DOWN:
                position = (position[0] - 1, position[1])
            guard_direction = transition[guard_direction]
        graph[position[0]][position[1]] = "X"
        cells_seen.add((position[0], position[1]))
        if guard_direction == direction.RIGHT:
            position = (position[0], position[1] + 1)
        elif guard_direction == direction.LEFT:
            position = (position[0], position[1] - 1)
        elif guard_direction == direction.UP:
            position = (position[0] - 1, position[1])
        elif guard_direction == direction.DOWN:
            position = (position[0] + 1, position[1])

    return graph, len(cells_seen)

def main():
    graph = get_input()
    path, cells = draw_path(graph)
    for row in path:
        print("".join(row))
    print(cells)

if __name__ == "__main__":
    main()



