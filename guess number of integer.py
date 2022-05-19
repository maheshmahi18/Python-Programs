import random
n=int(input("enter the no.of chances:"))
num=random.randint(1,10)
i=0
while (i<=n):
    g=int(input("enter the value:"))
    if i == n:
        print("Lost all chances")
        exit
    elif (g==num):
        print("Good.Guessed number is correct")
        break
    elif(g>num):
        print("Give lesser value")
    elif(g<num):
        print("Give greater value")
    i=i+1

        
