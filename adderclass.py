#AdderClass
class adder(object):
	#def __init__ (self):		#none of that overloading in python, y'hear me?
	#	self.value = 0
	def __init__ (self, val=None):		#use default values to simulate overriding however
		if val != None:
			self.value = val
		else:
			self.value=0
	def add (self, val):
		self.value += val
	def getValue(self):
		return self.value
	def passball(self):
		pass;