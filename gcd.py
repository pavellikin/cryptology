import sys

class GreatestCommonDivisor (object):
	result = []
	modulo = []
	x	   = [1,0]
	
	def __init__ (self, _divident, _divider):
		super(GreatestCommonDivisor , self).__init__()
		self.gcdCalculation(_divident, _divider)
		self.gcdLinearExpansion(_divident, _divider)


	def gcdCalculation (self, divident, divider):

		print("Started work with", divident, "and", divider)

		while 1:

			tmp = int (divident) % int (divider)

			if tmp ==0:
				break

			self.modulo.append (tmp)
			self.result.append (int (int (divident) / int (divider)))

			divident = divider
			divider  = self.modulo[len(self.modulo) - 1]

		print ("Results", self.result)
		print ("Modulos", self.modulo)


	def gcdLinearExpansion (self, divident, divider):
		
		while ((len (self.x) - 2) != len (self.modulo)):
			xResult = self.x[len(self.x) - 2] - self.result[len(self.x) - 2] * self.x[len(self.x) - 1]
			self.x.append (xResult)

		y = int ((self.modulo[len(self.modulo) - 1] + int(divident) * self.x[len(self.x) - 1]) / int(divider))

		print ("X      ", self.x[2:])
		print ("Y      ", y)

def help():
	print ("Usage: python3.2", sys.argv[0], "<divident> <divider>")
	exit()

####################################
#####      Program start       #####
####################################
if ((len(sys.argv) < 3) or (len(sys.argv) > 3)):
	help ()
elif (sys.argv[1] < sys.argv[2]):
	gcd = GreatestCommonDivisor(sys.argv[2], sys.argv[1])
else:
	gcd = GreatestCommonDivisor(sys.argv[1], sys.argv[2])