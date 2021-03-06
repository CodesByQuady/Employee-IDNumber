#Employee/ID Number Program. This program includes a secure version of the database.
#Updated from rough draft code in my notebook.

employees = {} #Empty Dictionary

def jobLog():
    while True: #This while loop is only if you want to control who can make changes to the database.
        admin = 'Admin'
        password = 'Password'
        print('Restricted User Access'.center(35,"="))#Helpful tip, adjusting strings using isleft(), isright(), center() will add some flare to your text.
        user = input('Username (Case Sensitive): ')
        if user != admin: #Login Fail
            print('Wrong User Login In Credentials, Try Again.')
            continue
        else:
            """Login Passed"""
            print('Hello',user,'Enter Your Password')
            uP = input('Password (Case Sensitive): ')
            if uP != password: #Second Login Step Failed
                print("Wrong Password Credentials, Try Again.")
                continue
            else:
                """Both Logins Are Correct, User Can Now Make Changes To The Database."""
                break
            break
    while True:
        print("""
Type a name to add or edit an employee file.
Press Enter to stop.
Enter p to print the employee database.
""")
        print('EMPLOYEE DATABASE'.center(35,"="))
        name = input('Name/(p): ')
        if name =='': #This conditon will end the program after printing the employees added or deleted from the database.
            for k, v in employees.items():
                print('Name',k,'Employee ID Number:',v)
            break
        
        if name in employees:#This condition will run if the name is already in the database
            for name in employees:
                print('EID:',employees[name])
                print("Would you like to remove this employee?")
                choice = input('Yes/No: ')
                if choice == 'Yes' or 'yes': #This subcode will allow the user to make changes to the dictionary if they want to. If not then it returns to the beginning of the program.
                    del employees[name]
                    print("Employee Is Removed From The Database.")
                    break
                elif choice == 'No' or 'no':
                    print("Action Cancelled, Returning To The Database.")
                    break
            else:
                print('Error, redirecting to the "EMPLOYEE_DATABASE".....')
        elif name == 'p':#This condition is to print the dictionary in case the user needs to know who is in the database.
            for k,v in employees.items():
                print("EMPLOYEES".center(35,"="))
                print("Name:",k,"EIN:",v)

        else: #This condition is what adds a key:value pair to the dictionary. Once the k:v pair is added, it can be changed or called. 
            print(name,': Record Is Not Found. What Is Employee ID Number?')
            number = input('EIN: ')
            employees[name] = number #This line of code will assign the value of the input() to the value of it's key in the dictionary.
            print(name,"Employee Database Is Updated.")

jobLog()
            

    
