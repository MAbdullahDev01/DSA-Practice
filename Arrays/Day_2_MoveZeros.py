# Problem: Move all zeros to the end of an array.
# Learning Objective: In-place array modification, two-pointer approach.

test_case_1 : list = [0, 0, 4, 0, 3, 4, 6, 9, 1]
test_case_2 : list = [0, 2, 4, 0, 3, 4, 7, 9, 0]
test_case_3 : list = [1, 0, 4, 0, 2, 0, 6, 0, 7]


def MoveZeros(num):
    writer = 0 # This pointer tracks the position to "write" the next non-zero number

    for reader in range(len(num)):
        if num[reader] != 0:
            num[writer], num[reader] = num[reader], num[writer]
            writer += 1
    print(num)

MoveZeros(test_case_1)
MoveZeros(test_case_2)
MoveZeros(test_case_3)

#Time Complexity: O(n)