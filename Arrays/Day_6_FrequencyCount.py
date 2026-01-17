# Problems: Count the frequency of elements in an array.
# Learning Objectives: Dictionary usage, frequency counting.

from utils.Random_List_Generator import randomListGenerator

def frequencyCount(numbers):

    # Initialise the dictionary
    numbers_count = {}

    # Iterate over every number
    for num in numbers:
        
        # If the num does not exist in the dictionary a new key-value pair is generated
        if num not in numbers_count:
            numbers_count[num] = 1

        # If the num exists in the dictionary the key-value pair is updated
        elif num in numbers_count:
            numbers_count[num] += 1
    return numbers_count


numbers = randomListGenerator(10, 0, 10)
print(numbers)
print(frequencyCount(numbers))

# Time Complexity: O(n)
# Space Complexity: O(n)