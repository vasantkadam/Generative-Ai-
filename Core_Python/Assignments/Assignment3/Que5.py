#7. Write a program to check if user has entered correct userid and password.
user_id='Vasant'
user_password="1234"

id=input("Enter the ID:")
pas=input("Enter the password:")
if user_id==id and user_password==pas:
    print("You Have Successfully login the Account")

else:
    print("Bhaiyaa Apka Password ya phir Id Galat hai ji ")
