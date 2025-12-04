##6. Write a program to find print the following Fibonacci series using
##functions:
##1 1 2 3 5 8 n terms

def fibo(n):
    a,b=1,1
    print(a,b,end=" ")
    for _ in range(n-2):
        c=a+b
        print(c,end=" ")
        a,b=b,c
n=int(input("Enter the number for fibbonacci sereis:"))
fibo(n)
