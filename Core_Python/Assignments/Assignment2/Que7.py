##Find the sum of three-digit number.

num=int(input("Enter the three Digit Number:"))

hundred=num // 100
tens=(num//10)%10
ones=num %10

total=hundred+tens+ones
print(f'Sum of Three Digits is:{total}')