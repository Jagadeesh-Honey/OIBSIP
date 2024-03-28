import random
import string

print("\t\t|||||RANDOM PASSWORD GENERATOR|||||\n")

def rapa():
    len=int(input("\nPrefer a Length for your Password : "))
    print("\nWhich type character do you want \n 1.Upper Case + Lower Case + Digits + Symbols \n 2.Only Upper Case + Digits + Symbols \n 3.Only LOwer Case + Digits + Symbols")
    op=int(input("Enter your Option : "))
    if(op == 1):
        pw = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation,k=len))
        print("\nYour PASSWORD is = "+pw)
    elif(op == 2):
        pw = ''.join(random.choices(string.ascii_uppercase+string.digits+string.punctuation,k=len))
        print("\nYour PASSWORD is = "+pw)
    elif(op == 3):
        pw = ''.join(random.choices(string.ascii_lowercase+string.digits+string.punctuation,k=len))
        print("\nYour PASSWORD is = "+pw)
    else:
        print("\nInvalid Option! Please try again")
        rapa()

rapa()
while(1):
    re=int(input("\nWould you like to Generate one more 1.YES 2.EXIT : "))
    if(re == 1):
        rapa()
    else:
        break
print("\n\t\tThankyou for Using this Password Generator")
#BY JAGADEESH honeyjagadeesh2@gmail.com
