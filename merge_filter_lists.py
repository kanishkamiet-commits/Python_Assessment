# Program: Merge Lists and Filter Numbers
# Question:
# Write a Python program to merge two lists, remove duplicate values,
# sort the final list in descending order, and display only those numbers
# that are divisible by both 3 and 5.

# Input first list
list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))

# Input second list
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

# Merge both lists
merged_list = list1 + list2

# Remove duplicates
unique_list = []

for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

# Sort list in descending order without using built-in sort()
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):
        if unique_list[i] < unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

# Display numbers divisible by both 3 and 5
print("\nNumbers divisible by both 3 and 5:")

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")