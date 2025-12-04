#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)
gender=input("Enter The Gender male/female:")
age=int(input("Enter the Age:"))

if age>21 and gender=='male':
    print("This boy is eligible for Marry ")
elif age>18 and gender=='female':
    print("This Girl is Eligible for marry")
else:
    print("Not Eligible for marry")
