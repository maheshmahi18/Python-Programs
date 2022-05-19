n=int(input("enter a number:"))
approx=0.5*n
better=0.5*(approx+n/approx)
while better != approx:
    approx=better
    better=0.5*(approx+n/approx)
print("The square root of a number=",round(approx,5))
