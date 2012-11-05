class GreatestCommonDivisor(object):
	
	def __init__(self, divident, divider):
		super(GreatestCommonDivisor , self).__init__()

		self.result = []
		self.modulo = []
		self.x	    = [1,0]
		self.gcdCalculation(divident, divider)


	def gcdCalculation(self, divident, divider):

		while 1:
			tmp = int (divident) % int (divider)
			
			if tmp == 0:
				break

			self.modulo.append(tmp)
			self.result.append(int (int (divident) / int (divider)))

			divident = divider
			divider  = self.modulo[len(self.modulo) - 1]


	def gcdLinearExpansion(self, divident, divider):
		
		while ((len (self.x) - 2) != len (self.modulo)):
			xResult = self.x[len(self.x) - 2] - self.result[len(self.x) - 2] * self.x[len(self.x) - 1]
			self.x.append (xResult)

		y = int ((self.modulo[len(self.modulo) - 1] + int(divident) * self.x[len(self.x) - 1]) / int(divider))

		print("X      ", self.x[2:])
		print("Y      ", y)