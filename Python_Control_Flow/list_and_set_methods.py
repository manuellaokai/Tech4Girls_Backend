#!usr/bin/python3
#list ()
my_list = [1, 3, 5, 7, 9]
print("Original list:", my_list)

# append()
my_list.append(11)
print("After append(11):", my_list)

# remove()
my_list.remove(5)
print("After remove(5):", my_list)

# extend()
my_list.extend([13, 15, 17])
print("After extend([13, 15, 17]):", my_list)

# Demonstrating set methods
my_set = {2, 4, 6, 8}
print("\nOriginal set:", my_set)

# add()
my_set.add(10)
print("After add(10):", my_set)

# remove()
my_set.remove(4)
print("After remove(4):", my_set)

# union()
another_set = {6, 8, 10, 12}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# intersection()
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# difference()
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

