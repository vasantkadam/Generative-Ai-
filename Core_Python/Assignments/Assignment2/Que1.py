##1. Convert the time entered in hh,min and sec into seconds.

H=int(input("Enter Hours:"))
T=int(input("Enter Minutes:"))
S=int(input("Enter the seconds:"))

Total_seconds=(H*3600)+(T*60)+S

print(f'Total seconds:{Total_seconds}')
