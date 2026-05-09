# Program: Set Operations
# Question:
# Write a Python program to perform union, intersection,
# symmetric difference, and subset operations on two sets
# entered by the user.

# Input first set
set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))

# Input second set
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

# Perform set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# Check subset
is_subset = set1.issubset(set2)

# Display results
print("\nUnion of sets:")
print(union_set)

print("\nIntersection of sets:")
print(intersection_set)

print("\nSymmetric Difference of sets:")
print(symmetric_difference_set)

print("\nSubset Check:")
if is_subset:
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")





'''output 
Enter elements of first set separated by space: 12
Enter elements of second set separated by space: 13

Union of sets:
{12, 13}

Intersection of sets:
set()

Symmetric Difference of sets:
{12, 13}

Subset Check:
First set is not a subset of second set.
'''   