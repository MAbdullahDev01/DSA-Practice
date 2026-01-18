# Problems: Calculate factorial of a number.
# Learning Objectives: Recursion basics, base case, recursion stack.

# What is recursion? A function calling itself.

def factorial(n):

    # If the user inputs 0 it should return 1
    if n == 0: # Base case
        return 1
    
    # Else using recursion the factorial of every number is calculated
    else:
        return n * factorial(n-1)
    

num = int(input("Enter a number to find its factorial: "))
print(factorial(num))

# Time Complexity: O(n)
# Space Complexity: O(n)