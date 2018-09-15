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
#lambda checker

def strAppender(n):		#n set in labmda fn envrion on call, and separate form n subsequently with this implementation
	return lambda x: n + x	#x + n was a prepender
qq=strAppender("q")
print(qq("q"))
rr=strAppender("r")
print(rr("age"))
n="s"	#should NOT affect the anonymous strAppender generated function
print(rr("ange"))

def strAppenderModifiable(n=""):
	"""Returns a lambda concatenation/addition function"""
	return lambda x, y=n: y+x;
tt=strAppenderModifiable("mod")
uu=strAppenderModifiable()
print("lambda fn: ",tt("ified"))
print(uu("ified", "mod"))
print(uu("ified"))
vv=strAppenderModifiable(2)
print(str(vv(6)))		#'+' is internally overridden by python
words = ['your', 'mother', 'hamster']
print(words)
for w in words:
	print(w,len(w))
for w in words[:]:
	if(w[0] in ("m","h")):
		words.insert(0,w)	#copy mother to 0th position
print("after inserting 'm' and 'h' words at the 0 position:",words)
print(" ".join(words))
print("compared to: ",*words)
#trying to dict(range(1,len(words)),words)
def unpackDict(d,i):
	return str(i) + d[i]
d={}
for i in range(1,len(words)):
	d[i]= words[i]
print("unpacking not totally useful dict: ",*[unpackDict(d,q) for q in d])
print("equivalent: :",*[str(q)+d[q] for q in d])
del words[:]	#dealloc the list by deallocing each element
#print("should error out: ", words) #and does!
