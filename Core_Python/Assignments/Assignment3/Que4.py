##6. Write a program to calculate profit or loss.
Sp=int(input("Enter the Selling Price:"))
Cp=int(input("Enter the cost price:"))

if Sp>Cp:
    profit=Sp-Cp
    print(profit,"Profit")
elif Cp>Sp:
    loss=Cp=Sp
    print(loss,"loss") 
else:
    print("No Profit No loss") 
      