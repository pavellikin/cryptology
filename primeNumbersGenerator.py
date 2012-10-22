class primeNumbersGenerator (object):
	def __init__(self, number):
		super(primeNumbersGenerator , self).__init__()
		self.primes = list(range(2, number + 1))
	
	#####################################
	### Sieve of Eratosthenes methood ###
	#####################################
	def sieveOfEratosthenes(self, number, divisor = 2):
		if (divisor ** 2) > number:
				print ("List of prime numbers: ", self.primes)
				return self.primes

		for i in self.primes:
			if i == divisor:
				continue
			if (i % divisor) == 0:
				self.primes.remove(i)

		divisor = self.primes[ self.primes.index(divisor) + 1]
		self.sieveOfEratosthenes (number, divisor)
