import sys
import residueClass

class Order(object):
	def __init__(self, number):
		super(Order , self).__init__()

		residueClasses = residueClass.ResidueClass(number)
		self.countingElementsOrder(residueClasses.reducedSystemOfResidues, number)

	def countingElementsOrder(self, Z, number):
		generatedElments = []
		for element in Z:
			_element = element

			for degree in Z:
				_element = element ** degree
				if _element > number:
					_element %= number
				generatedElments.append(_element)

			generatedElments = list(set(generatedElments))
			print ("ord", element, generatedElments)
			generatedElments = []

def help():
	print("Usage: python3.3 order.py <number>")

####################################
#####      Program start       #####
####################################
if len(sys.argv) < 2 or len(sys.argv) > 2:
	help()
else:
	order = Order(int (sys.argv[1]))