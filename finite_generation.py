class PandigitalGeneration(object):
	'''
	Generates all pandigital numbers.
	A pandigital number includes all digits 1 to 'n'.
	e.g. 213 is a 3-digit pandigital number.
	'''
	def __init__(self):
		import itertools as it

		digits = [1,2,3,4,5,6,7,8,9]
		perms = sorted([list(it.permutations(digits[:i], i)) for i in digits])
		self.pandigitals = ["".join(map(str, p)) for pp in perms for p in pp]

