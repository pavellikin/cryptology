import sys
import primeFactorDecomposition

class residueClass (object):
	def __init__(self, number):
		super(residueClass , self).__init__()

		decomposition = primeFactorDecomposition.PrimeFactorDecomposition(number)
		self.calculation(number, decomposition.result, 0)


	def calculation (self, number, decomposition, previousDecomposition = 0):
		if len(decomposition) == 0:
			print ("Residue classes:", int(number) - 1)
			return

		if previousDecomposition == decomposition[0]:
			tmp = number
		else:
			tmp = number * (1 - (1 / decomposition[0]))

		previousDecomposition = decomposition[0]
		self.calculation(tmp, decomposition [1:len(decomposition)], previousDecomposition)

def help():
	print("Usage: python3.3 residueClass.py <number>")

####################################
#####      Program start       #####
####################################
if len(sys.argv) < 2 or len(sys.argv) > 2:
	help()
else:
	residueClass = residueClass(int (sys.argv[1]))
		