# Exercise: Reverse a list without using the reverse() method
# Concepts: loops, lists, indexing

numbers : int = [1, 2, 3, 4, 5]
reversed_list : int = []
index : int = len(numbers) - 1

for _ in numbers:
    reversed_list.append(numbers[index])
    index -= 1

print(f"Original List: {numbers}")
print(f"Reversed List: {reversed_list}")