# Program: Sum of Digits using Recursive and Iterative Approaches
# Question:
# Write a recursive function to calculate the sum of digits
# of a given number and compare it with iterative approach.

# Recursive Function
def recursive_sum(n):

    # Base condition
    if n == 0:
        return 0

    # Recursive call
    return (n % 10) + recursive_sum(n // 10)


# Iterative Function
def iterative_sum(n):

    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


# Input number from user
number = int(input("Enter a number: "))

# Recursive result
recursive_result = recursive_sum(number)

# Iterative result
iterative_result = iterative_sum(number)

# Display results
print("\nSum of digits using Recursive Approach:", recursive_result)
print("Sum of digits using Iterative Approach:", iterative_result)

# Comparison
print("\nComparison:")
print("Recursive approach uses function calls and is shorter in code.")
print("Iterative approach uses loops and is generally faster and memory efficient.")




'''output
Enter a number: 12

Sum of digits using Recursive Approach: 3
Sum of digits using Iterative Approach: 3

Comparison:
Recursive approach uses function calls and is shorter in code.
Iterative approach uses loops and is generally faster and memory efficient.
'''