#8. Write a program find reverse of a number

def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
    
n=int(input("Enter the number:"))
print(reverse(n))
