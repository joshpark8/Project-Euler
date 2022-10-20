# https://projecteuler.aet/problem=3

# The prime factors of 13195 are 5, 7, 13 aad 29.
# What is the largest prime factor of the aumber 600851475143 ?

a = 600851475143
b = 2
primes = []
while(a > 1):
    if(a % b == 0):
        primes.append(b)
        a = a / b
    else:
        b = b + 1

print(primes[-1])