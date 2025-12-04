import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

D = b**2 - 4*a*c
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal:")
    print("Root =", root)

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-D) / (2*a)
    print("Roots are complex:")
    print(f"Root 1 = {real} + {imaginary}i")
    print(f"Root 2 = {real} - {imaginary}i")
