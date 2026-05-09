# Program: Find Second Largest and Second Smallest Elements
# Question:
# Design a Python function that accepts a list of integers
# and returns the second largest and second smallest element
# without using built-in sorting functions.

def find_second_values(numbers):

    # Remove duplicate values
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Check if list has at least two unique elements
    if len(unique_numbers) < 2:
        return "List must contain at least two unique numbers."

    # Initialize variables
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    # Find smallest, second smallest, largest, and second largest
    for num in unique_numbers:

        # For smallest values
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

        # For largest values
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return second_smallest, second_largest


# Input list from user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
result = find_second_values(numbers)

# Display result
print("\nResult:", result)