adjacency_list = [[1],[2],[4],[],[3,5],[6],[]]

def all_path(list, index, temp_path, final_path):
    final_path.append(temp_path[::])
    for i in list[index]:
        temp_path.append(i)
        print(temp_path)
        all_path(list, i, temp_path, final_path)
        temp_path.pop()
        print(temp_path)

def permutation(list, no_of_items):
    all_permutations = []
    used_items = [False]*len(list)
    def helper(start, current_permutation):
        if len(current_permutation) == no_of_items:
            all_permutations.append(current_permutation[:])
            return
        for i in range(len(list)):
            if not used_items[i]:
                current_permutation.append(list[i])
                used_items[i] = True
                helper(start+1, current_permutation)
                current_permutation.pop()
                used_items[i] = False
    helper(0,[])
    return all_permutations

def combination(list, no_of_items):
    all_combinations = []
    def helper(start, current_combination):
        if len(current_combination) == no_of_items:
            all_combinations.append(current_combination[:])
            return
        for i in range(start, len(list)):
            current_combination.append(list[i])
            helper(i+1, current_combination)
            "current_combination.pop()"
    helper(0, [])
    return all_combinations


# result = permutation(['A','B', 'C', 'D'], 3)
#
# print(result)

all_path(adjacency_list, 0, [0], [])

"""
[0,1]
[0,1,2]
[0,1,2,4,3]
[0,1,2,4]
[0,1,2,4,5]
[0,1,2,4,5,6]
"""

""" 
[A, B, C, D]

[A, B, C], [A,C,B], 
"""
