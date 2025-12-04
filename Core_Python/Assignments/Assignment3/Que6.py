##8. Write a program to prompt user to enter userid and password. After verifying
##userid and password display a 4 digit random number and ask user to enter the
##same. If user enters the same number then show him success message otherwise
##failed. (Something like captcha)
user_id='Vasant'
user_password="1234"

id=input("Enter the ID:")
pas=input("Enter the password:")
if user_id==id and user_password==pas:
    print("You Have Successfully login the Account")

else:
    print("Bhaiyaa Apka Password ya phir Id Galat hai ji ")

code=2142
c=int(input("Enter The Code for Verification:"))
if code==c:
    print("You verified Successfully")
else:
    print("Apne code Galat dala hai ji :)")  
