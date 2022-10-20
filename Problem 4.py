# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

limit = 999
palindromes = []

for i in range(1, limit):
    for j in range(1, limit):
        x = i * j
        if str(x) == str(x)[::-1]:
            palindromes.append(x)

print(max(palindromes))