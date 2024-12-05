def find_valid(content):
    count = 0
    for line in content:
        #print(line)
        line_list = list(map(int, line.split(" ")))
        
        ascending = descending = True 
        
        prev = float("-inf")
        for c in line_list:
            if c > prev:
                prev = c
            else:
                ascending = False 

        prev = float("inf")

        for c in line_list:
            if c < prev:
                prev = c
            else:
                descending = False 

        if not ascending and not descending:
            #print("neither condition holds")
            continue

        prev = line_list[0] 

        valid = True 
        for c in line_list[1:]:
            if 1 <= abs(prev - c) <= 3:
                prev = c 
            else:
                valid = False
                print("distance is", abs(prev - c))
                break
        if not valid:
            continue
        count += 1

    print(count)

with open("input1.txt", 'r') as file:
    content = file.readlines()
    find_valid(content)

#find_valid("""7 6 4 2 1
#1 2 7 8 9
#9 7 6 2 1
#1 3 2 4 5
#8 6 4 4 1
#1 3 6 7 9""".split("\n"))





