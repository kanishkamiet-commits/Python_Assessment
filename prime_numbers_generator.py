# Program: Prime Numbers Generator
# Question:
# Create a program that generates the first N prime numbers using a for loop
# and also calculates the sum and average of those prime numbers.

# Input value of N
n = int(input("Enter the value of N: "))

prime_numbers = []
num = 2

# Generate first N prime numbers
while len(prime_numbers) < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(num)

    num += 1

# Calculate sum and average
total = sum(prime_numbers)
average = total / n

# Display results
print("\nFirst", n, "prime numbers are:")
print(prime_numbers)

print("\nSum of prime numbers:", total)
print("Average of prime numbers:", average)