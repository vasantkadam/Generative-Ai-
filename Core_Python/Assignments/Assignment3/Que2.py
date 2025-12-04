##2. Write a program to input any alphabet and check whether it is vowel or consonant.

ch=input("Enter the Alphabet: ")
ch=ch.lower()

if ch in['a','e','i','o','u']:
    print(ch,"is the vovel")

else:
    print(ch,"is consonant")
    