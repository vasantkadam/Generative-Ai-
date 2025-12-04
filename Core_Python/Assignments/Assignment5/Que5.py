##5. Write a program to accept an integer amount from user and tell minimum

ammount=int(input("Enter the amoount"))

notes=(500,200,100,50,20,10,5)
 
print("The Minimun Notes required:")

for i in notes :
    count=ammount//i
    if count>0:
        print(i,"X",count)
    ammount%=i
    