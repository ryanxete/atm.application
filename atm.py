balance = 44337
def desired_number():
    return print("please enter the desired number!")
def thanks():
    return print("thanks for your business.")
def deposit(balance, num):
            balance += num
            print(f"new balance: ${balance}")
            thanks()
def withdraw(balance, num):
            balance -= num
            print(f"new balance: ${balance}")
            thanks()
username = input("create a username! ")
password = input("create a password! ")
print("you are now registered!")
print("to login please enter your username and password!")
question = True
while question is True:
    login_username = input("username? ")
    if username == login_username:
        print("enter your password now!")
        break
    else:
        print("wrong username! please try again.")
while question is True:
    login_password = input("password? " )
    if password == login_password:
        print("you are now logged in! welcome to your account.")
        break
    else:
         print("wrong password! please try again.")
print("please choose one the options below\n1: check your balance\n2: change username/password\n3: deposit funds\n4: withdraw funds\n5: logout from your account")
func11 = desired_number()
option = int(input())
while question is True:
    if option == 1:
        print(f"your balance at this time is: ${balance}")
        thanks()
        break
    elif option == 2:
        print("in order to change your credentials, choose the number that applies:\n1: change your username\n2: change your password")
        func11 = desired_number()
        option2 = int(input())
        if option2 == 1:
            new_user = input("enter your new username.")
            print("done")
            break
        elif option2 == 2:
            new_user = input("enter your new password.")
            print("done")
            break
    elif option == 3:
        num = int(input("enter the amount trying to deposit! "))
        deposit(balance, num)
    elif option == 4:
        num = int(input("enter the amount trying to withdraw! "))
        withdraw(balance, num)
    else:
        thanks()
        break