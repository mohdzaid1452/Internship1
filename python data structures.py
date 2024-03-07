#1
""" def flatten_tuple(tuple):

  
  flattened_tuple = ()
  for i in tuple:
    for element in i:
      flattened_tuple += (element,)
  return flattened_tuple


tuple = ((1, 2, 3), (4, 5, 6))
flattened_tuple = flatten_tuple(tup)
print(flattened_tuple)  """

#2
""" def set_to_tuple(s):
    return tuple(s)

def tuple_to_set(t):
    return set(t)


set_example = {1, 2, 3, 4, 5}
tuple_example = (6, 7, 8, 9, 10)

tuple_from_set = set_to_tuple(set_example)
set_from_tuple = tuple_to_set(tuple_example)

print("Tuple from set:", tuple_from_set)
print("Set from tuple:", set_from_tuple)
 """

#3
""" 
def sort_tuple_list_by_nth_element(tuple_list, n):
    return sorted(tuple_list, key=lambda x: x[n])

# Example usage:
tuple_list = [(1, 5, 3), (2, 2, 2), (3, 1, 4), (4, 3, 1)]
sorted_tuple_list = sort_tuple_list_by_nth_element(tuple_list, 1)
print(sorted_tuple_list) """
""" 
#4
def list_of_dicts_to_tuple_list(list_of_dicts):
    tuple_list = []
    for dictionary in list_of_dicts:
        tuple_list.append(tuple(dictionary.items()))
    return tuple_list

# Example usage:
list_of_dicts = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4},
    {'e': 5, 'f': 6}
]

tuple_list = list_of_dicts_to_tuple_list(list_of_dicts)
print(tuple_list) """

#5
""" def find_tuple_indices(tuple_list_1, tuple_list_2):
    # Create a dictionary mapping each tuple from tuple_list_2 to its index
    tuple_dict = {tuple(item): index for index, item in enumerate(tuple_list_2)}
    
    # Find indices of tuples from tuple_list_1 in tuple_dict
    indices = [tuple_dict.get(tuple(item), None) for item in tuple_list_1]
    
    return indices

# Example usage:
tuple_list_1 = [(1, 2), (3, 4), (5, 6)]
tuple_list_2 = [(7, 8), (3, 4), (9, 10), (1, 2), (11, 12)]

indices = find_tuple_indices(tuple_list_1, tuple_list_2)
print("Indices:", indices) """

#6
""" dict = [{'Gfg' : [5, 6, 5]}, {'is' : [10, 2, 3]}, {'best' : [4, 3, 1]}] 
 

print("The original list is : " + str(dict))
 

res =[{} for idx in range(len(dict))]
idx = 0
for sub in dict:
    for key, val in sub.items(): 
        for ele in val:
            res[idx][key] = ele
            idx += 1
        idx = 0
         
# printing result 
print("Records after conversion : " + str(res))
 """