# Problem: Find the maximum and minimum in an array.
# Learning Objectives: Array traversal, comparison, Python max, min.

from utils.Random_List_Generator import randomListGenerator

# Generate a random list
num_list = randomListGenerator(15, 1, 100)
print("Random List:", num_list)

# Manual max/min calculation
# Time complexity for manual solution is: O(n)
max_value = num_list[0]
min_value = num_list[0]

for num in num_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print(f"Maximum value is: {max_value}")
print(f"Minimum value is: {min_value}")

# Optional: Using built-in functions
print("Using built-in functions:")
print("Max:", max(num_list))
print("Min:", min(num_list))