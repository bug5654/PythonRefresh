#AdderClass
class adder(object):
	#def __init__ (self):		#none of that overloading in python, y'hear me?
	#	self.value = 0
	def __init__ (self, val=None):
		if val != None:
			self.value = val		#non-functional?
		else:
			self.value=0			#seemingly always called, with or without val being declared
	def add (self, val):
		self.value += val
	def getValue(self):
		return self.value