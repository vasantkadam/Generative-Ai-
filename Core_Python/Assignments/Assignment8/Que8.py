##9. Write a program to check if entered number is a palindrome or
#not.

def palindrom(n):
    return n==int(str(n)[::-1])
n=int(input("Enter the Number"))

if palindrom(n):

    print("Number is palindrom")
else:
    print("Not Plaindrom")
    