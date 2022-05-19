def isPrime(num):
    if num==2:
        return True
    elif num<2 or not num%2:
        return False
    for i in range(3,int(num**.5+1),2):
        if not num%i:
            return False
    return True
def generatePrimes(n):
    primes=[2,]
    noOfPrimes=1
    testNum=3
    while noOfPrimes<n:
        if isPrime(testNum):
            primes.append(testNum)
            noOfPrimes +=1
        testNum +=2        
    return primes
result=generatePrimes(int(input("Enter a n value to print n primenumbers:")))
print(result)
