# Problems: Find the second largest number in an array.
# Learning Objective: Sorting concepts, comparison logic.

from utils.Random_List_Generator import randomListGenerator

test_case_1 = randomListGenerator(10, 1, 100)
test_case_2 = randomListGenerator(10, 1, 100)
test_case_3 = randomListGenerator(10, 1, 100)

print(test_case_1)
print(test_case_2)
print(test_case_3)

def findSecondLargest(test):

    # Sorting the array in ascending form using built in fucntion
    test.sort()

    # Initializing variable
    largest = test[-1]
    second_largest = 0

    # Looping over the array to find the second largest 
    for i in range(len(test), -1, -1):
        if test[i - 1] < largest:
            second_largest = test[i - 1]
            break
    
    print(f"Second largest is {second_largest}")

# Time Complexity: O(n log n)
# Space Complexity: O(1)

findSecondLargest(test_case_1)
findSecondLargest(test_case_2)
findSecondLargest(test_case_3)