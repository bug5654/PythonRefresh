print("String analysis program")
stringVar = "  Greetings Program!  "
stringVarReset = stringVar

print("string in question: '" + stringVar + "'")
print( "type: " + str( type(stringVar) ) )
print( "number of 'e's: " + str(stringVar.count("e")) )
print( "position of 'P': " + str(stringVar.find('P')) )
#confirmed: 0-based string position (C-style)
print( "lowercase: " + stringVar.lower() )
print( "uppercase: " + stringVar.upper() )
print( "e->q: " + stringVar.replace('e','q') )
stringVar = stringVarReset
print( "strip whitespace: " + stringVar.strip() )
print( "positions 3-5: " + stringVar[3:5])
print( "remove last 3 characters: " + stringVar[:-3] )
print( "first 10 characters alternate route: %.10s" % stringVar)

randNum=951.0372486
print("non-rounded float: %f" % randNum)
print("rounded float: %.2f" % randNum)
a = "C:\some\thing\near"
print("accidental backslash usage:\n",a)
a = r"C:\some\thing\near"
print("corrected via r'...' raw quote:\n",a)
print("multiline using backslashes for clarity:\n")
s="""\
My bologna has a first name
It's O-S-C-A-R
My bologna has a second name
It's M-A-Y-E-R
"""
print(s*3+"Oscar Mayer bologna!","At your supermarket now!")	###
	#replacing + with , yields a space at beginning of line visible & desirable between the second two strings
alt = ("My bologna has a first name\n" "It's O-S-C-A-R\n" 
	"My bologna has a second name\n" "It's M-A-Y-E-R\n")	###
	#putting string literals in parens concatenates them, but only exact literals
print(alt+"Should look familiar")
print("slicing (listing every index):",\
	alt[3],alt[4],alt[5],alt[6],alt[7],alt[8],alt[9])
print("slicing the easy way(range): ",alt[3:10])	#don't forget [min,max)
print("does it work backwards? ",alt[9:2:-1])	#have to specify step since min>max still [min,max) though
print("back to:",a)
print("len is string length in python:",len(a))
print("but it's one based:",a[:len(a)])		#would cut off a letter if len 0-based
print("remember though, strings are immutable in python")
b=a[:14]+r"wicked\this\way\comes"
print("so create a new string instead:",b)
a,b,c = ["d","e","f"] #multiple assignment
print(a,b,c)

#string literals
print("str v repr:",str(alt),"repr:",repr(alt))
import math
print(f'pi is legally {math.pi:.2f}.')	#string format in string
print("mathematically it's more like {0}".format(round(math.pi,15)))
print("there are other approximations:")
approxs = {"22/7":22/7, "333/106":333/106, "16/15":16/15}
for title, fraction in approxs.items():
	print(f"{title:10} ~= {fraction:1.8f}")

#iterators
s = "a string"
it = iter(s)
print("iterator after creation:",it)
while True:
	try:
		print("next(it):",next(it))
	except(StopIteration):
		print("StopIteration occured!")
		break;

import random

class randomLetterGen:
	"""pulls random letters from a string"""
	
	def __init__(self, stringer):
		self.used = []
		self.genString=stringer

	def __iter__(self):
		return self;

	def __next__(self):
		if(len(self.used) == len(self.genString)):	#catch error on blank genString
			raise StopIteration
		distinct = False
		while distinct == False:
			index = random.randint(0,len(self.genString)-1)
			if index in self.used:
				continue
			self.used.append(index)
			yield self.genString[index]
			if(len(self.used) == len(self.genString)):
				raise StopIteration		#stops hanging

r = randomLetterGen("Bass Cannon")
print("Base string: Bass Cannon")
try:
	for char in r.__next__():
		print("random letter from gen:",char)
except:
	print("caught Exception!")
