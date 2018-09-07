#AdderClass
class adder(object):
	def __init__ (self):
		self.value = 0
	def add (self, val):
		self.value += val
	def getValue(self):
		return self.value