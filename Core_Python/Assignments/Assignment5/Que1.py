#1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
id="Vasant"
password=1234

attempts=3

for i in range(attempts):
    user_id=input("Enter your id:")
    user_pass=int(input("Enter the user password:"))

    if user_id==id and user_pass==password:
        print("you login succesfully")
        break
    else:
        print("Incorrect input")
else:
    print("Too many attemps Try later")

