# Exercise: Print all numbers greater than 10 in a list
# Concept: lists, loops, conditionals

numbers : int = [5, 12, 7, 20, 1, 15]

for num in numbers:         # Iterates over the list.
    if num > 10:            # Checks if the number is greater than 10.
        print(num)