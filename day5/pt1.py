from collections import defaultdict
import sys, math
def parse_input(input_file):
    with open(input_file, "r") as f:
        input = f.readlines()
        new_line = input.index("\n")

        pre_requisites = input[:new_line]
        nums_before = defaultdict(list)
        for line in pre_requisites:
            fst, snd = line.split("|")
            #print(f"fst {fst}, second {snd}")
            nums_before[int(fst)].append(int(snd)) #tlls us nums which cant appears
        return nums_before, input[new_line+1:]

def main():
    graph, after = parse_input(sys.argv[1]) 
    print(after)
    valid = count_valid(graph, after)
    print(f"total if {valid}")
    return valid

def count_valid(graph, after):
    valid_num = 0
    print("antireqs are", graph)
    for line in after:
        seen = set()
        all_works = True
        for word in line.split(","):
            seen.add(int(word))
            anti_reqs = graph[int(word)]

            for req in anti_reqs:
               if req in seen:
                   all_works = False
            
        if not all_works:
            continue
        else:
            print(f"{line} Line works")
            middle_index = math.ceil(len(line.split(","))/2)
            print("split line", line.split(","))
            print(f"middle index is {middle_index}")
            valid_num += int(line.split(",")[middle_index - 1])
    
    return valid_num
                   







if __name__ == "__main__":
    main()