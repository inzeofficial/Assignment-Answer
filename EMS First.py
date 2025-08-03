                      #!!!!!!!!!!!! START MY FIRST ASSIGNMENT!!!!!!!!!!!!!!!!!!!!!!

"""
                                           Employee Management System (EMS)
"""
# Step 1: Data Storage using Dictionary
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

# Step 2: Define the Menu System
# We Use The Loops Here For Add, View, Search, Exit.
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

# This Loop Is Works When The Person Enter The Option Given The Above Code
# When Person Enter 1 Then Code Is Run And Add The New Employee In The Dictionary.
# If Person Enter 2 Then Show All Employee Store In The Dictionary.
# If Person Enter 3 Then Search For Employee And Give The Result Whatever You Want And Searching For The Employee.
# And Last Is 4 This Is Use For Exit From The Code.

# Step 3: Add Employee Functionality
# This Code Is Use For Add New Employee.
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please try a different ID.")
            return
# This Code Is Use For Add New Employees.
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
# When Person Enter Above Option Then All The Value Store In Below Dictionary.
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully!")
# This Code Activated When The Person Enter The Incorect Value.
    except ValueError:
        print("Invalid input. Please enter the correct data types.")

# Step 4: View All Employees
# This Code Is Use For The Show The Result Of All The Store Value In The Dictionary.
def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("----------------------------------------------")
    for emp_id, info in employees.items():
        print(f"{emp_id}\t{info['name']}\t{info['age']}\t{info['department']}\t{info['salary']}")

# Step 5: Search for an Employee by ID
# This Code Is Use For Searching A Employee By Enter The Employee ID.
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee Found:\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Please enter a valid Employee ID.")

# Step 6: Start the Program
if __name__ == "__main__":
    main_menu()
#                      !!!!!!THANK YOU FOR THE INTERESTING PROJECT!!!!!!
