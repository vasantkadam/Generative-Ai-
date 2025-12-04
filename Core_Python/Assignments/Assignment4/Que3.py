##3. WAP to print sum of series upto n.
n=int(input("Enter the Number of n:"))
sum_series=0
print("sum numebrs from 1 to ",n,"are:")

for i in range (1,n+1):
    sum_series+=i

    print(sum_series)