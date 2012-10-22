import sys
import primeNumbersGenerator

class PrimeFactorDecomposition (object):

	def __init__ (self, number):
		super(PrimeFactorDecomposition , self).__init__()
		print("Programm started with number", number)
	
		self.result = []
		primeGenerator = primeNumbersGenerator.primeNumbersGenerator(number)
		primeGenerator.sieveOfEratosthenes(number, 2)

		if number in primeGenerator.primes:
			print ("Number is prime", number)
			return
		else:
			self.calculation(number, primeGenerator.primes[0:len(primeGenerator.primes)])
			print ("Number decomposition:", self.result)


	def calculation (self, number, primes):
		tmp = 0
		_prime = primes[0]

		if number == 1:
			return

		if (number % _prime) == 0:
			tmp = number / _prime
			self.result.append(_prime)
			_prime = primes
		else:
			tmp = number
			_prime = primes[1:len(primes)]

		self.calculation (tmp, _prime)