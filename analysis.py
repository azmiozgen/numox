class Analysis(object):

	def __init__(self, number):

		self._number = number
		if self._number < 0:
			return "Not valid for analysis"
		elif self._number == 0:
			self._primeFactors = []
			self._factors = []
			return None
		elif self._number == 1:
			self._primeFactors = []
			self._factors = [1]
			return None
		self._factorize()

	def _factorize(self):
		'''
		Creates the prime factors and prime representation of given number.
		'''
		import itertools
		import numpy as np

		self._primeFactors = []

		## Division by 2
		number = self._number
		while number % 2 == 0:
			self._primeFactors.append(2)
			number /= 2

		## Division by odd numbers
		for i in xrange(3, number + 1, 2):

			## Continue if the number 'i' is multiple of any element in the 'primes'.
			for prime in list(set(self._primeFactors)):
				if i % prime == 0:
					break
			else:
				## Append 'i' to primeFactors
				while number % i == 0:
					number = number / i
					self._primeFactors.append(i)

				## All factors
				self._factors = [1,]
				for i in xrange(1, len(self._primeFactors) + 1):
					nn = set(itertools.combinations(self._primeFactors, i))
					nn = np.array(list(nn))
					for n in nn:
						self._factors.append(n.prod())
				self._factors.sort()
			continue

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

