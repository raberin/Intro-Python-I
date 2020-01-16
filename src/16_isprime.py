"""
Write a program to determine if a number, given on the command line, is prime.

   1. How can you optimize this program?
   2. Implement [The Sieve of
      Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
      of the oldest algorithms known (ca. 200 BC).
"""

import sys


def is_prime_unoptimized(num):
    if num == 2 or num == 3 or num == 5:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    else:
        return True

def is_prime_optimized(num):

print(is_prime(int(sys.argv[1])))
