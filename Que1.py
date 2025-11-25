n=int(input("Enter the number:"))
count = 0
num=2
while count < n:
    is_prime=True
    i = 2
    while i * 1 <= int(num**0.5):
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
