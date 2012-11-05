import primeFactorDecomposition
import gcd

class ResidueClass (object):
	def __init__(self, number):
		super(ResidueClass , self).__init__()

		decomposition = primeFactorDecomposition.PrimeFactorDecomposition(number)

		self.residueClasses = 0
		self.reducedSystemOfResidues = [1]
		if decomposition.primeNumberFlag == True:
			self.residueClasses = number - 1
			self.reducedSystemOfResidues = list(range(1, number))
			print ("Residue classes:", self.residueClasses, self.reducedSystemOfResidues)
		else:
			self.calculation(number, decomposition.result, 0)
			self.getReducedSystem(number)
			print ("Residue classes:", self.residueClasses, self.reducedSystemOfResidues)


	def getReducedSystem(self, number):
		greatestCommonDivisor = 0
		for i in list(range(1, number)):
			if i == 1:
				continue

			greatestCommonDivisor = gcd.GreatestCommonDivisor(number, i)
			if 1 in greatestCommonDivisor.modulo:
				self.reducedSystemOfResidues.append(i)


	#######################
	### Euler`s theorem ###
	#######################
	def calculation(self, number, decomposition, previousDecomposition = 0):
		if decomposition == []:
			self.residueClasses = int(number)
			return

		if previousDecomposition == decomposition[0]:
			_number = number
		else:
			_number = number * (1 - (1 / decomposition[0]))

		previousDecomposition = decomposition[0]
		self.calculation(_number, decomposition[1:len(decomposition)], previousDecomposition)
		