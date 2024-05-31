# List operations
my_list = [6,4,2]
print("Original list:", my_list)
my_list.append(5)
print("List after adding an element:", my_list)
my_list.remove(2)
print("List after removing an element:", my_list)
my_list[1] = 4
print("List after modifying an element:", my_list)

# Dictionary operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)
my_dict['a'] = 23
print("Dictionary after modifying a value:", my_dict)

# Set operations
my_set = {6,4,2}
print("\nOriginal set:", my_set)
my_set.add(5)
print("Set after adding an element:", my_set)
my_set.remove(2)
print("Set after removing an element:", my_set)
my_set.remove(4)
my_set.add(8)
print("Set after modifying elements:", my_set)
