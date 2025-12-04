#WAP to print factorial of a number .

n=int(input("Enter the Number of n:"))
fact=1

for i in range (1,n+1):
    fact *=i

print(f'factorial of 1 to {n} is {fact}')
