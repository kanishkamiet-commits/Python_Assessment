# Program: Inventory Management System
# Question:
# Develop a dictionary-based inventory management system
# where users can add products, update quantity,
# search products, and display low-stock items.

# Create empty inventory dictionary
inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Search Product")
    print("4. Display Low-Stock Products")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Product
    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity

        print("Product added successfully.")

    # Update Product Quantity
    elif choice == 2:
        product = input("Enter product name to update: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Quantity updated successfully.")
        else:
            print("Product not found.")

    # Search Product
    elif choice == 3:
        product = input("Enter product name to search: ")

        if product in inventory:
            print("Product:", product)
            print("Quantity:", inventory[product])
        else:
            print("Product not found.")

    # Display Low-Stock Products
    elif choice == 4:
        limit = int(input("Enter low-stock limit: "))

        print("\nLow-Stock Products:")

        found = False

        for product, quantity in inventory.items():
            if quantity < limit:
                print(product, ":", quantity)
                found = True

        if not found:
            print("No low-stock products found.")

    # Exit
    elif choice == 5:
        print("Exiting Inventory Management System.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")



''' output
  ===== Inventory Management System =====
1. Add Product
2. Update Product Quantity
3. Search Product
4. Display Low-Stock Products
5. Exit
Enter your choice: 1
Enter product name: pen
Enter quantity: 10
Product added successfully.

===== Inventory Management System =====
1. Add Product
2. Update Product Quantity
3. Search Product
4. Display Low-Stock Products
5. Exit
Enter your choice: 4
Enter low-stock limit: 3

Low-Stock Products:
No low-stock products found.
'''     