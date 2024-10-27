#!usr/bin/python3

original_string = "Hello, World!"
upper_string = original_string.upper()
print("Original string:", original_string)
print("Uppercase string:", upper_string)

lower_string = original_string.lower()
print("\nOriginal string:", original_string)
print("Lowercase string:", lower_string)

replaced_string = original_string.replace("World", "Python")
print("\nOriginal string:", original_string)
print("Replaced string:", replaced_string)

list_of_strings = ["Python", "is", "fun"]
joined_string = " ".join(list_of_strings)
print("\nList of strings:", list_of_strings)
print("Joined string:", joined_string)
