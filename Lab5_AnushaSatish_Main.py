import Lab5_AnushaSatish_Function

function_file = Lab5_AnushaSatish_Function


def main():
    print('**' * 50)
    print(' ' * 25, "Employee Operations")
    print('**' * 50)
    choice = function_file.menu()
    print(choice)
    while choice != 6:
        if choice == 1:
            function_file.print_all()
            choice = function_file.menu()

        elif choice == 2:
            find_fname = input('Enter in a FName to search employee')
            find_lname = input('Enter in a LName to search employee')
            find_emp = find_fname + " " + find_lname
            function_file.print_emp(find_emp)
            choice = function_file.menu()

        elif choice == 3:
            function_file.add_emp()
            choice = function_file.menu()

        elif choice == 4:
            del_fame = input('Enter in a FName to delete employee')
            del_lname = input('Enter in a LName to delete employee')
            del_emp = del_fame + " " + del_lname
            function_file.delete_emp(del_emp)
            choice = function_file.menu()

        elif choice == 5:
            mod_fname = input('Enter in a FName to modify employee')
            mod_lname = input('Enter in a LName to modify employee')
            mod_emp = mod_fname + " " + mod_lname
            function_file.modify_emp(mod_emp)
            choice = function_file.menu()

    function_file.exit_app()


if __name__ == "__main__":
    main()
