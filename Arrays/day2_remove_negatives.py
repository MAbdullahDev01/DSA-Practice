# Exercise: Create a new list by removing all the negative numbers
# Concepts: lists, loops, conditionals

numbers : int = [-3, 5, -1, 0, 12, -9, 7]
positive_numbers : int = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)