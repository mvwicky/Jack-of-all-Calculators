class Operations(object):
	inputs = []
	def __init__(self , args):
		n = 0
		a = len(args)
		while n < a:
			self.inputs.append(args[n])
			n += 1

	def addition(self):
		n = 1
		a = len(self.inputs)
		s = self.inputs[0]
		while n < a:
			s += self.inputs[n]
			n += 1
		return s

	def subtraction(self):
		n = 1
		a = len(self.inputs)
		s = self.inputs[0]
		while n < a:
			s -= self.inputs[n]
			n += 1
		return s

	def multiplication(self):
		n = 1
		a = len(self.inputs)
		s = self.inputs[0]
		while n < a:
			s *= self.inputs[n]
			n += 1
		return s

	def division(self):
		n = 1
		a = len(self.inputs)
		s = self.inputs[0]
		while n < a:
			s /= self.inputs[n]
			n += 1
		return s
