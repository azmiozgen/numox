class PrimeGeneration(object):
	'''
	Generates prime numbers.
	First two primes are automatically generated.
	'''
	def __init__(self):
		self._primes = [2, 3]
		self.factorize()

	def next(self):
		'''
		Returns next prime number.
		'''
		candidate = self._primes[-1] + 2
		while True:
			for prime in self._primes:
				if (candidate % prime) == 0:
					break
			else:
				self._primes.append(candidate)
				break
			candidate += 2
		self.factorize()
		return self._primes[-1]

	def factorize(self):
		'''
		Find all combinations of current primes.
		'''
		import itertools
		import numpy as np

		self._factors = [1,]
		for i in xrange(1, len(self._primes) + 1):
			nn = set(itertools.combinations(self._primes, i))
			nn = np.array(list(nn))
			for n in nn:
				self._factors.append(n.prod())
		self._factors.sort()

	def getPrimes(self):

		return self._primes

	def getFactors(self):

		return self._factors

class BinomialGeneration(object):
	'''
	Generates binomial number series.
	First two binomial series are automatically generated.
	'''
	def __init__(self):
		self._binomials = [(1), (1, 1)]

	def next(self):
		'''
		Returns next binomial series.
		'''
		nextBinom = [1]
		for i in xrange(len(self._binomials[-1]) - 1):
			middle = self._binomials[-1][i] + self._binomials[-1][i + 1]
			nextBinom.append(middle)
		nextBinom.append(1)
		self._binomials.append(nextBinom)
		return nextBinom

	def getBinomials(self):

		return self._binomials

class RightTriangleGeneration(object):
	'''
	Generates integer right triangle side lengths.
	'''
	def __init__(self):
		self.sides = [(3, 4, 5)]
		self._hypoCandidateSet = range(1, 7)

	def next(self):
		'''
		Returns next right triangle sides tuple.
		'''
		from math import sqrt

		squares = map(lambda x:x**2, self._hypoCandidateSet)
		found = False
		while not found:
			for square1 in squares[:-1]:
				for square2 in squares[:-1]:
					if square1 + square2 == squares[-1]:
						newSideSet = [sqrt(square1), sqrt(square2), sqrt(squares[-1])]
						newSideSet = tuple(map(int, newSideSet))
						self.sides.append(newSideSet)
						found = True
						break
				if found == True:
					break
			hypoCandidate = self._hypoCandidateSet[-1] + 1
			self._hypoCandidateSet.append(hypoCandidate)
			squares.append(hypoCandidate ** 2)
		return newSideSet

