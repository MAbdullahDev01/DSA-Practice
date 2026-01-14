# Problem: Check if a string is a palindrome.
# Learning Objective: String traversal, conditional logic.

test_case_1 = "racecar"
test_case_2 = "level"
test_case_3 = "noun"
test_case_4 = "abbbba"

def isPalindrome(text):
    is_palindrome = False
    pointer1 = 0

    for pointer2 in range(len(text), -1, -1):
        if pointer1 == len(text) // 2:
            is_palindrome = True
            break
        elif text[pointer1] == text[pointer2 - 1]:
            pointer1 += 1
        else:
            break

    if is_palindrome:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

isPalindrome(test_case_1)
isPalindrome(test_case_2)
isPalindrome(test_case_3)
isPalindrome(test_case_4)

# Time Complexity: O(n)
# Space Complexity: O(1)