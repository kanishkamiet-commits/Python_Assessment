# Program: Menu-Driven Banking Application
# Question:
# Write a menu-driven banking application using a while loop
# that allows users to deposit, withdraw, check balance,
# and exit only when the user chooses the exit option.

# Initial balance
balance = 0

# Start menu loop
while True:
    print("\n===== Banking Menu =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Deposit option
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", balance)

    # Withdraw option
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

        print("Current Balance:", balance)

    # Check balance option
    elif choice == 3:
        print("Current Balance:", balance)

    # Exit option
    elif choice == 4:
        print("Thank you for using the banking application.")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")