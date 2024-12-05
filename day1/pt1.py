


left = []
right = []
with open("input.txt", 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)


left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print("distance: ", dist)
