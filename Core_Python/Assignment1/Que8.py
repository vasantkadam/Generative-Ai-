days=int(input("Enter the NUmber of Days:"))

years=days//365

days_remain=days%365

weeks=days_remain//7
days_left=days_remain%7

print(f'Years:{years}')
print(f'weeks:{weeks}')
print(f'Days:{days_left}')