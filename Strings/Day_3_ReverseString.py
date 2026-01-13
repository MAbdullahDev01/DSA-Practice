# Problem: Reverse a list without using slicing.
# Learning Objectives: Loop traversal, building a new list, index handling.

from utils.Random_List_Generator import randomListGenerator

def reverseList(original_list):
    reversed_list = []

    # Traverse from last index to first
    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])

    return reversed_list

# Time Complexity: O(n)
# Space Complexity: O(n)

nums = randomListGenerator(15, 1, 100)
print("Original list:", nums)

reversed_nums = reverseList(nums)
print("Reversed list:", reversed_nums)
