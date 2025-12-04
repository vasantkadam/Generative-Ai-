##Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1=int(input("Enter The marks of subject1:"))
s2=int(input("Enter the marks of subject2:"))
s3=int(input("Enter the marks of subject3:"))
s4=int(input("Enter the marks of subject4:"))
s5=int(input("Enter the marks of subject5:"))

total=s1+s2+s3+s4+s5

if total>350:
    print("First Class")
elif total>250:
    print("seconf class")
else:
    print("Third class")    