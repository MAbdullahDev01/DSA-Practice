# Exercise: Find the maximum and minimum in a list
# Concepts: loops, lists, conditional statements, comparison

numbers : int = [5, 2, 9, 1, 7]
min_num : int = numbers[0] # Assume first element is max
max_num : int = numbers[0] # Assume first element is min

for num in numbers:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

print(f"Minimum number of the list is : {min_num}")
print(f"Maximum number of the list is : {max_num}")