# Created by Marley Sexton, 2024
# GNU Public License

import sympy
import math
import mpmath

def is_odd(number):	# check if a number is odd
	if number % 2 != 0: # it is odd
		return True
	else: # if number % 2 == 0, is is even
		return False

def count_digits(base, exp):	# count how many digits a number has, d=log10(a^b)
    return int(mpmath.log10(mpmath.power(base, exp))) + 1
	
def full_prime_test(n):
    #print("... attempting Miller-Rabin test")
    if sympy.ntheory.primetest.mr(n, base_set):
        #print("PASSED \n... attempting Strong Lucas PRP test")
        if sympy.ntheory.primetest.is_strong_lucas_prp(n):
            #print("PASSED")
            return True
    
    return False

# ----------------------------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------------------------

primefile = open("Euler_Drift_Primes_n_less_than_10000.txt", "w+")
primefile.write("base, exponent, drift, digits, exponent_prime")
n = 1
while n < 10000:
    e = math.e	# define Eulers number
    test = mpmath.floor(mpmath.power(e,n)) # generate starting test number = floor(e^n)
    test = int(test) # turn the test into a integer number
    #print("Testing e^{}".format(n), end="")
    is_odd_yn = False			
    if is_odd(test) is True:
        if full_prime_test(test):
            c = count_digits(e, n)
            print("e^{} is PRIME!".format(n))
            primefile.write("e,{},0,{}\n".format(n,c))
        else:
        	is_odd_yn = True
    else:
        if is_odd(test) is False:
            #print("... SKIPPING [Even number]")
        
        skip = False
        if is_odd_yn is True:
        	m = 2	# if e^n is odd, move up/down in 2s (to another odd number)
        else:
        	m = 1	# if e^n is even, move up/down in 2s, with an initial offset of 1 (to another odd number)
        while True:
           # print("Testing drift e^{} +/- {} ... ".format(n,m))
            #print("[Testing +{} drift]".format(m))
            if full_prime_test(test+m):
                c = count_digits(e, n)			# count digits
                m_prime = full_prime_test(m)	# attempt full prime test
                print("e^{}+{} is PRIME! {} digits, exp_prime? {}".format(n,m,c,m_prime))
                primefile.write("e,{},+{},{},{}\n".format(n,m,c,m_prime))
                skip = True						# if a prime is found, "skip" to next value of n
            # print("[Testing -{} drift]".format(m))
            if full_prime_test(test-m):
                c = count_digits(e, n)			# count digits
                m_prime = full_prime_test(m)	# attempt full prime test
                print("e^{}-{} is PRIME! {} digits, exp prime? {}".format(n,m,c,m_prime))
                primefile.write("e,{},-{},{},{}\n".format(n,m,c,m_prime))
                skip = True						# if a prime is found, "skip" to next value of n
            if skip is True:
                break
            m += 2   # increment drift
    n += 1	# increment exponant
