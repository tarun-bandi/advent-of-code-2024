
from collections import Counter

left = []
right = []
with open("input.txt", 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)


left.sort()
right.sort()

counts = Counter(right)
dist = 0
for i in range(len(left)):
    cur = left[i]
    ct = counts[cur]
    dist += ct * cur
print("distance: ", dist)
