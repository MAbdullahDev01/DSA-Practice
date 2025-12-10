# Exercise: Count how many numbers in a list are even and print the total count
# Concepts: loops, lists, conditional, counting

numbers : int = [2, 3, 4, 8, 11, 14]
count : int = 0 # Initialise a counter

for num in numbers:
    if not num % 2:         # When a number is even the result of num % 2 will be zero but the not converts the result to 1 meaning true
        count += 1

print(f"Total number of even numbers are: {count}")