import random

def findFibonacci(n):
    if n==0 or n==1: #F(0)=0,F(1)=1
        return n
    else: #F(n)=F(n-1)+F(n-2)
        return findFibonacci(n-1)+findFibonacci(n-2)

def FermatTheoremPrime(a,p): # a^(p-1) = 1 mod p
    return pow(a, p-1, p) == 1

n = int(input("Enter number for nth Fibonacci: "))
x = findFibonacci(n)
print("Chack if %d is prime" %x)

for i in range(1,20):
    a = random.randint(1,x-1)
    if FermatTheoremPrime(a,x)==0:
        print("Not prime")
        quit()
print("Is prime")
