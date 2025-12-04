p=float(input("Enter the Principle ammount:"))
T=float(input("Enter the Time:"))
R=float(input("Enter the Rate:"))

A = p*(1 + R/100)**T

CI=A-p
print(f'Compaound Intrest:{CI}')
