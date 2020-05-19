import os

def menu():
    choice = 0
    print('\n')
    print('--' * 20, " Menu ", '--' * 20)
    while choice == 0:
        try:
            choice = int(input('\n Enter Menu choice '
                               '\n 1. To display gross PR payroll report for all employees '
                               '\n 2. To display a gross PR payroll report for a single employee by name'
                               '\n 3. To add an employee record'
                               '\n 4. To delete an employee record'
                               '\n 5. To modify an employee record'
                               '\n 6. Exit '))
        except ValueError:
            choice = 0
            print("Please enter a numeric value")
    return choice


def print_all():
    try:
        org_file = open("employee.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        return
    line_no = org_file.readline()
    while line_no != "":
        print('**' * 25)
        line_no = line_no.split(" ")
        rate = float(line_no[2])
        hours = float(line_no[3])
        gross = float(rate * hours)
        if hours >= 40:
            ot_hours = hours - 40
            ot_pay = rate * ot_hours * 1.5
            print()
        else:
            ot_pay = 0
        print("First Name : "+line_no[0])
        print("Last Name : "+line_no[1])
        print("Gross Pay : $"+format(gross, '.2f'))
        print("Overtime Pay : $"+format(ot_pay, '.2f'))
        line_no = org_file.readline()
    org_file.close()


def print_emp(find_emp):
    try:
        org_file = open("employee.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        return
    line = org_file.readline()
    counter = 0
    while line != "":
        line = line.split(" ")
        rate = float(line[2])
        hours = float(line[3])
        if find_emp.lower() == (line[0] + " " + line[1]).lower():
            counter = 1
            print('**' * 25)
            gross = float(rate * hours)
            if hours >= 40:
                ot_hours = hours - 40
                ot_pay = rate * ot_hours * 1.5
            else:
                ot_pay = 0
            print("First Name : " + line[0])
            print("Last Name : " + line[1])
            print("Gross Pay : $" + format(gross, '.2f'))
            print("Overtime Pay : $" + format(ot_pay, '.2f'))
        line = org_file.readline()
    if counter == 0:
        print("Not found !!")
    else:
        org_file.close()


def add_emp():
    try:
        file = open("employee.txt", 'a')
        file_read = open("employee.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        return
    emp_fname, emp_lname, emp_pay, emp_hours = "", "", "", ""
    emp_fname = input('Please enter Employee First name to add')
    emp_lname = input('Please enter Employee Last name to add')
    emp_fullname = emp_fname+" "+emp_lname
    line_count = file_read.readline()
    counter = 0
    for line_count in file_read:
        line_count = line_count.split(" ")
        if emp_fullname.lower() == (line_count[0] + " " + line_count[1]).lower():
            print("Sorry Can't add employee !!! Details already exists")
            counter = 1

    if counter == 0:
        while emp_pay == "":
            try:
                emp_pay = float(input('Please enter Employee pay to add'))
            except ValueError:
                emp_pay = ""
                print("You have entered an incorrect value!!! Employee pay should be a number")

        while emp_hours == "":
            try:
                emp_hours = float(input('Please enter Employee working hours '))
            except ValueError:
                emp_hours = ""
                print("You have entered an incorrect value!!! Working hours should be a number")

        new_emp = emp_fname + " " + emp_lname + " " + str(emp_pay) + " " + str(emp_hours)
        print("Adding details ..", new_emp)
        file.write("\n" + new_emp)
        file.close()
        file_read.close()


def delete_emp(del_emp):
    temp_file = open("temp.txt", 'w')
    try:
        org_file = open("employee.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        return
    count = 0
    for line_count in org_file:
        check_str = line_count.split(" ")
        if del_emp.lower() != (check_str[0] + " " + check_str[1]).lower():
            temp_file.write(check_str[0] + " " + check_str[1] + " " + check_str[2] + " " + check_str[3])
        else:
            count = 1
            print("Deleting employee details....")

    if count == 0:
        print("Employee Details not found!! ")
    else:
        temp_file.close()
        org_file.close()
        os.remove("employee.txt")
        os.rename("temp.txt", "employee.txt")


def modify_emp(mod_emp):
    temp_file = open("temp.txt", 'w')
    try:
        org_file = open("employee.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        return
    check_name = 0
    mod_pay, mod_hours = "", ""
    for traverse in org_file:
        s_list = traverse.split(" ")
        if (mod_emp.lower()) == (s_list[0] + " " + s_list[1]).lower():
            check_name = 1
            while mod_pay == "":
                try:
                    mod_pay = float(input('Please enter Employee pay to modify'))
                except ValueError:
                    mod_pay = ""
                    print("You have entered an incorrect value!!! Employee pay should be a number")

            while mod_hours == "":
                try:
                    mod_hours = float(input('Please enter Employee working hours to modify'))
                except ValueError:
                    mod_hours = ""
                    print("You have entered a incorrect value!!! Working hours should be a number")
            new_details = str(s_list[0] + " " + s_list[1] + " " + str(mod_pay) + " " + str(mod_hours))
            print("Modifying details of ", mod_emp)
            temp_file.write(new_details + "\n")
        else:
            temp_file.write(s_list[0] + " " + s_list[1] + " " + s_list[2] + " " + s_list[3] + "\n")
    if check_name == 0:
        print("Employee Details not found!! ")
    else:
        temp_file.close()
        org_file.close()
        os.remove("employee.txt")
        os.rename("temp.txt", "employee.txt")


def exit_app():
    print("Ending..")
    exit(0)
