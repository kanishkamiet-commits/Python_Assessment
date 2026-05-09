# Program: Employee Records Using Tuples
# Question:
# Create a program that stores employee records in tuples.
# Each tuple should contain employee ID, name, and salary.
# Display employees whose salary is above the average salary.

# Input number of employees
n = int(input("Enter number of employees: "))

employees = []
total_salary = 0

# Store employee records
for i in range(n):
    print(f"\nEnter details for Employee {i + 1}")

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    # Create tuple
    employee = (emp_id, name, salary)

    # Add tuple to list
    employees.append(employee)

    total_salary += salary

# Calculate average salary
average_salary = total_salary / n

# Display average salary
print("\nAverage Salary:", average_salary)

# Display employees with salary above average
print("\nEmployees with salary above average:")

for employee in employees:
    if employee[2] > average_salary:
        print("Employee ID:", employee[0])
        print("Employee Name:", employee[1])
        print("Employee Salary:", employee[2])
        print()







''' output
 Enter number of employees: 2

Enter details for Employee 1
Enter Employee ID: 1
Enter Employee Name: khushi
Enter Employee Salary: 120000

Enter details for Employee 2
Enter Employee ID: 2
Enter Employee Name: kanishka
Enter Employee Salary: 100000

Average Salary: 110000.0

Employees with salary above average:
Employee ID: 1
Employee Name: khushi
Employee Salary: 120000.0
'''