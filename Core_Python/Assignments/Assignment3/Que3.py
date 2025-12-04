##3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input("Enter the first Angle: "))
b=int(input("Enter the Second Angle: "))
c=int(input("Enter the Third Angle: "))

if a>0 and b>0 and c>0 and(a+b+c==180):
    print("This Traingle is valid ")
else:
    print("This Traingle is not valid ")
