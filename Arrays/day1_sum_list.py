# Exercise: Sum all numbers in a list
# Concepts: loops, lists, accumulation

numbers : int = [4, 5, 8, 9, 2, 0, 9, 4] 
total : int = 0                  # Initialise accumulator

for num in numbers:              # Iterates over the list
    total += num                 # Totalling

print (f"Sum of the list is: {total}")