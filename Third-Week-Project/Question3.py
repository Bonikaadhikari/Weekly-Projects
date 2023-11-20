#Write a program to find if the given number is prime or not.

def isPrime(n):
    if(n<2):
        raise ValueError("Provide number greater than two")

    for i in range(2, n):
        if(n%i==0):
            return False
    
    return True
n = int(input("Provide a number"))
if(isPrime(n)):
    print(n, "is a prime number ")
else:
    print(n, "is not a prime number")


