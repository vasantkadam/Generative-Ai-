n=int(input("Enter the Number of employee:"))

total_salary=0

for i in range(1,n+1):
    base=int(input("Enter the base salary:"))

    if base<20000:
        da=base*0.1
        ta=base*0.12
        hra=base*0.15
    else:
        da=base*0.15
        ta=base*0.18
        hra=base*0.20

    total=da+ta+hra+base
    print(f"Total salary of emp {i} = {total}")
    total_salary+=total

print(f'Total Salary of All employee:{total_salary}')

