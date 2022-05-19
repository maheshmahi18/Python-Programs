n=int(input("enter n:"))
r=int(input("enter r:"))
def power(n,r):
    if n==0: return 0
    elif r==0: return 1
    elif r==1: return n
    elif r%2==0:
        res_even=power(n,r/2)
        return res_even*res_even
    else:
        res_odd=power(n,(r-1)/2)
        return n*res_odd*res_odd
pow=power(n,r)
print("The power of",n,"&",r,"is",pow)
