class Analysis(object):

	def __init__(self, number):

		self._number = number
		if self._number < 0:
			return "Not valid for analysis"
		self._number = number
		self._primeFactors = []
		if self._number == 0:
			self._factors = []
			return None
		if self._number == 1:
			self._factors = [1]
			return None
		self._factors = []
		self._factorize()

	def _factorize(self):
		'''
		Creates the prime factors and prime representation of given number.
		'''
		import itertools
		import numpy as np

		n = self._number
		i = 2
		while i ** 2 <= n:
			if n % i:
				i += 1
			else:
				n //= i
				self._primeFactors.append(i)
		if n > 1:
			self._primeFactors.append(n)

		## All factors
		for i in xrange(1, len(self._primeFactors) + 1):
			nn = set(itertools.combinations(self._primeFactors, i))
			nn = np.array(list(nn))
			for n in nn:
				self._factors.append(n.prod())
		self._factors.sort()

	def printAsPrimes(self):
		'''
		Shows as multiples of its primes.
		'''
		print "{} =".format(self._number),
		if self._number == 0:
			print 0
		elif self._number == 1:
			print 1
		for i in xrange(len(self._primeFactors)):
			if i != len(self._primeFactors) - 1:
				print "{} x".format(self._primeFactors[i]),
			else:
				print self._primeFactors[i]

	def getNumber(self):

		return self._number

	def getPrimeFactors(self):

		return self._primeFactors

	def getFactors(self):

		return self._factors

	def isPrime(self):

		return len(self._factors) == 2

	def isPalindromic(self):

		return str(self._number)[::-1] == str(self._number)

	def isAmicable(self):
		'''
		Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
		If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
		'''
		j = Analysis(sum(self._factors[:-1]))
		if j._number == self._number:
			return False
		return sum(j._factors[:-1]) == self._number
