# EDP = EULER DRIFT PRIMES

Basic Python 3.11 script to generate "Euler Drift Primes". 
Requires sympy, math, and mpmath modules

Euler Drift Primes are here defined to be the the smallest value of m, such that p is prime, where p = floor(e^n) +- m for a given integer value of n.
The program outputs a basic text file with comma seperated values of e, n, m, number of digits, and whether the exponent itself is prime.

This script utilizes an initial Miller-Rabin primality test, followed by a Strong Lucas Probable Prime (SLP) test, to probabilistically determine the primality of a given number.

The full process is as follows:
1. Take a positive integer value of n.
2. Calculate e^n, and then floor the value
3. Check if e^n is prime (if so, start with a new value of n)
4. if e^n is not prime, then test (e^n)+m and (e^n)-m, where m starts at 1 if e^n is even, and 2 if e^n is odd.
5. If (e^n)+m and *e^n)-m is not prime, increment m by 2, and then reattempt until a prime is found.

For example, e^930 is not prime, but by incrementing m, we discoveer that the closest prime is e^930-301 (404 digits)

1 million digit primes roughly start at n = 250000. 

Provided without warrenty. Crashes when it runs out of RAM! 
