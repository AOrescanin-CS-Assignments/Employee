#****************************************************************************************************
#
#       Name:       Alex Orescanin
#       File:       employeeDriver.py
#       Description:
#               This program uses the Employee class to perform tasks
#
#       Other files included: Employee.py
#
#****************************************************************************************************

import Employee
import pickle

#****************************************************************************************************

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
LINE = 50
FILENAME = 'employees.dat'

def main():
    emp1 = Employee.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    emp2 = Employee.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    emp3 = Employee.Employee('Joy Rodgers', '81774', 'Manufacturing', 'Engineer')

    empDict = {emp1.get_id(): emp1, emp2.get_id(): emp2, emp3.get_id(): emp3}

    choice = 0
    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(empDict)

        elif choice == ADD:
            add(empDict)

        elif choice == CHANGE:
            change(empDict)

        elif choice == DELETE:
            delete(empDict)

    save_employee(empDict)

#****************************************************************************************************

def load_employees():
    try:
        infile = open(FILENAME, 'wb')
        dict = pickle.load(infile)
    except IOError:
        dict = {}

    return dict

#****************************************************************************************************

def get_user_choice():
    print('Menu')
    print('-' * LINE)
    print('1. Look up an employee\n2. Add a new employee\n'
          '3. Change an existing employee\n4. Delete an employee\n'
          '5. Quit the program\n')

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        print('Error invalid choice')
        choice = int(input('Enter your choice'))

    return choice

#****************************************************************************************************

def look_up(empDict):
    empID = input('Please enter an employee ID number: ')
    print(empDict.get(empID, 'An employee with that ID does not exist\n'))

#****************************************************************************************************

def add(empDict):
    name = input('Enter employee name: ')
    id = input('Enter employee ID: ')
    dep = input('Enter employee department: ')
    job = input('Enter employee title: ')

    if id in empDict:
        print('An employee with that ID already exists')
    else:
        emp = Employee.Employee(name, id, dep, job)
        empDict[id] = emp
        print('Employee was added\n')

#****************************************************************************************************

def change(empDict):
    id = input('Enter an employee ID number: ')

    if id in empDict:
        name = input('Enter new employee name: ')
        dep = input('Enter new employee department: ')
        job = input('Enter new employee title: ')
        del empDict[id]
        emp = Employee.Employee(name, id, dep, job)
        empDict[id] = emp
    else:
        print('An employee with that ID does not exist/n')

#****************************************************************************************************

def delete(empDict):
    empID = input("Enter employee ID number: ")
    if empID in empDict:
        del empDict[empID]
        print('Employee was deleted\n')
    else:
        print('An employee with that ID does not exist\n')

#****************************************************************************************************

def save_employee(empDict):
    outfile = open(FILENAME, 'wb')
    pickle.dump(empDict, outfile)
    outfile.close()

#****************************************************************************************************

if __name__ == '__main__':
    main()

#****************************************************************************************************
# Sample Output:
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 1
# Please enter an employee ID number: 47899
# Name: Susan Meyers
# ID Number: 47899
# Department: Accounting
# Title: Vice President
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 2
# Enter employee name: Alex
# Enter employee ID: 47899
# Enter employee department: IT
# Enter employee title: Programmer
# An employee with that ID already exists
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 2
# Enter employee name: Alex
# Enter employee ID: 16369
# Enter employee department: IT
# Enter employee title: Programmer
# Employee was added
#
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 1
# Please enter an employee ID number: 555
# An employee with that ID does not exist
#
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 1
# Please enter an employee ID number: 16369
# Name: Alex
# ID Number: 16369
# Department: IT
# Title: Programmer
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 3
# Enter an employee ID number: 555
# An employee with that ID does not exist/n
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 3
# Enter an employee ID number: 16369
# Enter new employee name: Alexander
# Enter new employee department: Security
# Enter new employee title: Police Officer
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 1
# Please enter an employee ID number: 16369
# Name: Alexander
# ID Number: 16369
# Department: Security
# Title: Police Officer
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 4
# Enter employee ID number: 555
# An employee with that ID does not exist
#
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 4
# Enter employee ID number: 16369
# Employee was deleted
#
# Menu
# --------------------------------------------------
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee
# 4. Delete an employee
# 5. Quite the program
#
# Enter your choice: 5
#
# Process finished with exit code 0
#****************************************************************************************************