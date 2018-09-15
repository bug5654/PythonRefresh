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
print("words without an ending ",words.pop(), ": ",words)		#pop goes off before the print
print("and without a beginning ",words.remove("hamster"),": ",words)
print("how many mothers in words: ", words.count("mother"))
print("index of first mother: ",words.index("mother"))
print("index of second mother: ",words.index("mother",words.index("mother")+1))
words.sort()
print("words sorted:", words)
words.reverse()
print("reversed after sorting: ",words)
words.append("hamster")
words.insert(0,"hamster")
print("added hamsters back in: ",words)

def listSwapInPlace(l,a,b):
	if(b>a):	#make sure pos1 < pos2 so the +1 grabs the item to be swapped
		pos1,pos2=a,b
	else:
		pos1,pos2=b,a
	l.insert(pos1,l[pos2])
	l.insert(pos2,l[pos1+1])
	l.pop(pos1+1)
	l.pop(pos2+1)
	return l
listSwapInPlace(words,1,2)
print("swapping 1 and 2: ",words)	#done this way to ensure words actually changed, despite return value

del words[:]	#dealloc the list by deallocing each element
#print("should error out: ", words) #and does!
