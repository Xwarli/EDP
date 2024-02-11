import sympy
import math
import mpmath

def is_odd(number): # check if a number is odd
	if number % 2 != 0: # it is odd
		return True
	else: # if number % 2 == 0, is is even
		return False

def count_digits(base, exp):	# count how many digits a number has, d=log10(a^b)
	return int(mpmath.log10(mpmath.power(base, exp))) + 1
	
def full_prime_test(n):
	base_set = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087] 
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
		#if is_odd(test) is False:
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
			m += 2	 # increment drift
	n += 1	# increment exponant
	
	
