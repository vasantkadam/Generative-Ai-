#WAP to calculate selling price of book based on cost price and discount.
CP=int(input("Enter the Cost Price Ammount:"))
Discount=int(input("Enter the Discount in precentage:"))

discount_ammount=(Discount/100)*CP

SP=CP-discount_ammount

print(f'Selling Price BAsed on the discount and cost price is:{SP}')
