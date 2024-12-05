def find_valid(content):
    """
    Helper Function that determines if an array is safe based on the original
    given rules
    """
    count = 0
    for line in content:
        line_list = list(map(int, line.split(" ")))
        
        ascending = descending = True 
        rmIndx1 = rmIndx2 = -1
        prev = float("-inf")
        for i, c in enumerate(line_list):
            if c > prev:
                prev = c
            elif rmIndx1 == -1:
                rmIndx1 = i
            else:
                ascending = False 

        prev = float("inf")
        if not ascending:
            for i, c in enumerate(line_list):
                if c < prev:
                    prev = c
                elif rmIndx2 == -1:
                    rmIndx2 = i
                else:
                    descending = False 

        if not ascending and not descending:
                continue
            
        prev = line_list[0] 
        
        start = 0 
        if rmIndx2 == 0 or rmIndx1 == 0: 
            start = 1
        valid = True 
        prev = line_list[start]
        for j, c in enumerate(line_list[1+start:]):
            idx = j + 1 + start
            if (ascending and rmIndx1 == idx or descending and rmIndx2 == idx):
                continue 
            if 1 <= abs(prev - c) <= 3:
                prev = c 
            elif (ascending and rmIndx1 == -1) or (descending and rmIndx2 == -1):
                rmIndx1 = rmIndx2 = 0
            else:
                valid = False
                break
        if not valid:
            continue
        count += 1

    print("Number of safe arrays: ", count)

with open("input1.txt", 'r') as file:
    content = file.readlines()
    find_valid(content)

find_valid("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n"))





