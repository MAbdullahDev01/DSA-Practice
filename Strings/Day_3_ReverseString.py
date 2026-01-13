# Problem: Reverse a string without using slicing.
# Learning Objectives: String manipulation, loops, building new string.

from utils.Random_List_Generator import randomListGenerator

def reverseList(orignal_list):
    reversed_list = [] # Initializing an empty list

    for i in range(len(orignal_list), 1, -1):
        reversed_list.append(orignal_list[i - 1])
    reversed_list.append(orignal_list[0])
    print(reversed_list)

# Time complexity: O(n)

num = randomListGenerator(15, 1, 100) # Generating a random list of integers
print(num)

reverseList(num) # Calling the reverseList function