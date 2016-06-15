class DualAnalysis(object):

	def __init__(self, number1, number2):

		self.number1 = number1
		self.number2 = number2
		if self.number1 < 0 or self.number2 < 0:
			return "Not valid for analysis"

	def greatestCommonDivider(self):
		'''
		Finds greatest common divider of two numbers using Euclid's algorithm.
		'''
		while self.number2 != 0:
			temp = self.number1;
			self.number1 = self.number2;
			self.number2 = temp % self.number2;
		return self.number1;

	def areRelativePrime(self):
		'''
		Answers if two number are relatively prime.
		Relatively primes have no common divisor other than 1.
		'''
		return self.greatestCommonDivider() == 1
