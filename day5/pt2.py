from collections import defaultdict
import sys, math
def parse_input(input_file):
    with open(input_file, "r") as f:
        input = f.readlines()
        new_line = input.index("\n")

        pre_requisites = input[:new_line]
        nums_after = defaultdict(list)
        graph_comp = defaultdict(list)
        for line in pre_requisites:
            fst, snd = line.split("|")
            #print(f"fst {fst}, second {snd}")
            nums_after[int(snd)].append(int(fst)) #tlls us nums which cant appears
            graph_comp[int(fst)].append(int(snd))
        return nums_after, input[new_line+1:], graph_comp

def main():
    graph, after, complement = parse_input(sys.argv[1]) 
    # print(after)
    valid = count_valid(graph, after, complement)
    print(f"total if {valid}")
    return valid

def count_valid(graph, after, complement):
    valid_num = 0
    # print("antireqs are", graph)
    for line in after:
        seen = set()
        all_works = True
        for word in line.split(","):
            seen.add(int(word))
            pre_reqs = complement[int(word)]

            for req in pre_reqs:
               if req in seen:
                   all_works = False
            
        if not all_works:
            #Topologically sort the line 
            print("trying to sort:",line)
            in_degree = defaultdict(int)

            queue = []
            for word in line.split(","):
                in_degree[int(word)] = len(set.intersection(set(graph[int(word)]), seen))
            # print("in degree", in_degree)
            # print("graph", graph)
            for node in in_degree:
                if in_degree[node] == 0:
                    queue.append(node)
                
            list_sorted = []
            while queue:
                node = queue.pop(0)
                for neighbour in complement[node]:
                    in_degree[neighbour] -= 1
                    if in_degree[neighbour] == 0:
                        queue.append(neighbour)
                list_sorted.append(node)
            
            if len(list_sorted) == len(line.split(",")):
                middle_index = math.ceil(len(line.split(","))/2)

                print(f"middle index: {middle_index -1}, middle value is is {line.split(',')[middle_index - 1]} in array of size {len(line.split(","))}")
                valid_num += int(list_sorted[middle_index - 1])   
                print("sorted", list_sorted)
            else:
                print("not sorted, no soritng executed", list_sorted)


    
    return valid_num
                   







if __name__ == "__main__":
    main()