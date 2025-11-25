n=int(input("Enter the number:"))

sumof_serires=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact *=j
    sumof_serires+=i/fact

print(f'sum of sereis:{sumof_serires}')
