import primeNumbersGenerator

class PrimeFactorDecomposition(object):

	def __init__(self, number):
		super(PrimeFactorDecomposition , self).__init__()
		print("Programm started with number:", number)
	
		self.result = []
		self.primeNumberFlag = False
		primeGenerator = primeNumbersGenerator.PrimeNumbersGenerator(number)
		primeGenerator.sieveOfEratosthenes(number, 2)

		if number in primeGenerator.primes:
			print("Number is prime")
			self.primeNumberFlag = True
			return
		else:
			self.decomposition(number, primeGenerator.primes[0:int(len(primeGenerator.primes)/2)])
			print("Number decomposition:", self.result)


	def decomposition(self, number, primes):
		_number = 0
		_prime = primes[0]

		if number == 1:
			return

		if (number % _prime) == 0:
			_number = number / _prime
			self.result.append(_prime)
			_prime = primes
		else:
			_number = number
			_prime = primes[1:len(primes)]

		self.decomposition(_number, _prime)