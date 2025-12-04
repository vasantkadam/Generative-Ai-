#12. Write a program to check if given 3 digit number is a palindrome or not.

num=input("Enter the Three Digit Number:")

if num == num[::-1]:
    print(num,"The Number Is palindrom")

else:
    print(num,"The number Is not palindorm")
