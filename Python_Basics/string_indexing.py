#!usr/bin/python3

sentence = "Python is powerful and easy to learn."
print("Length of the sentence:", len(sentence))

first_character = sentence[0]
print("First character:", first_character)

last_character = sentence[-1]
print("Last character:", last_character)

start_index = sentence.index("powerful")
end_index = start_index + len("powerful")
word_powerful = sentence[start_index:end_index]
print("The word 'powerful':", word_powerful)


