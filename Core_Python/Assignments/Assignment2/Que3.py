##3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))


meters_from_feet =feet*0.3048

cm_from_inches = inches*2.54
total_cm = cm_from_inches+(meters_from_feet*100)
meters = int(total_cm//100)
centimeters=total_cm%100

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)

