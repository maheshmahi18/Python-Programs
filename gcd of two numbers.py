n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))
if n1>n2:
    smaller=n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if((n1%i==0) and (n2%i==0)):
      gcd=i
print("The GCD o",n1,",",n2,"is:",gcd)
