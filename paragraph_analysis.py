# Program: Paragraph_analysis
# Question:
# Write a Python program that accepts a paragraph from the user
# and calculates the number of uppercase letters, lowercase letters,
# digits, spaces, and special characters.
# Display the result in descending order based on frequency.

def analyze_text(paragraph):
    counts = {
        "Uppercase Letters": 0,
        "Lowercase Letters": 0,
        "Digits": 0,
        "Spaces": 0,
        "Special Characters": 0
    }

    # Count different types of characters
    for char in paragraph:
        if char.isupper():
            counts["Uppercase Letters"] += 1
        elif char.islower():
            counts["Lowercase Letters"] += 1
        elif char.isdigit():
            counts["Digits"] += 1
        elif char.isspace():
            counts["Spaces"] += 1
        else:
            counts["Special Characters"] += 1

    # Sort in descending order based on frequency
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_counts


# Accept paragraph input from user
text = input("Enter a paragraph:\n")

# Analyze text
results = analyze_text(text)

# Display output
print("\nCharacter count in descending order:")

for category, count in results:
    print(f"{category}: {count}")