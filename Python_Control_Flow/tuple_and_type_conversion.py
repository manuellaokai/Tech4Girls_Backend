#!usr/bin/python3

# Define a tuple containing 5 different elements
my_tuple = (42, "Hello", 3.14, True, None)
print("Tuple:", my_tuple)

# Use indexing to print the first and last elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Demonstrate the use of count() and index() methods
print("Count of 'Hello':", my_tuple.count("Hello"))
print("Index of 3.14:", my_tuple.index(3.14))

# Type conversions
# Convert an integer to a float
int_value = 100
float_value = float(int_value)
print("Integer to float:", float_value)

# Convert a float to an integer
float_value = 9.99
int_value = int(float_value)
print("Float to integer:", int_value)

# Convert a string representing a number to an integer
string_number = "123"
int_from_string = int(string_number)
print("String to integer:", int_from_string)

# Join a list of strings into a single string
string_list = ["Python", "is", "awesome"]
joined_string = " ".join(string_list)
print("Joined string:", joined_string)
