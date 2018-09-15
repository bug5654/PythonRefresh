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

from collections import deque
q = deque(["larry", "moe"])
print("original q:",q)
q.append("curly")
print("curly q:",q)
print("q without",q.popleft()," as list: ",list(q))

squares = list(map(lambda x: x**2, range(3)))
#squares = [x**2 for x in range(3)]		#same as above, preferred
print("first 3 squares: ",squares)
del squares[:]
squares = [(x,x**2) for x in range(3)]
print("now as tuples with index:",squares)

testlist = [[1,2], 3]
print("testlist:",testlist)
print("type of testlist:",str(type(testlist)))
#[num for elem in testlist for num in elem if type(elem)=="List" else num=elem]
def flatten(src):	#recursion not 100% yet
	print("		INIT - src:",src)
	for l in src:
		if type(l)==list:
			lindex = src.index(l)
			for q in l:
				print("		LOOP - src",src,"q:","lindex:",lindex)
				if(type(q)==list):
					print("RECURSED!")
					flatten(q)	#recursion to flatten any depth of list
				src.insert(lindex,q)
				lindex+=1
			else:
				src.pop(lindex)	#put in else to emphasize continuity

flatten(testlist)
print("flattened testlist: ", testlist)
torturelist = [1,[2],[[3]],[[4,5,[6]]]]
print("torturelist:",torturelist)
flatten(torturelist)
print("flattened torturelist",torturelist)

#import itertools
#flattenedList = list(itertools.chain(*torturelist))
#print("itertools flattened list: ", flattenedList)
#above approach not working on toture list
print("list(zip(torture)):",list(zip(torturelist))) #not what we want

#sets
animals = {'cat','dog','canary'}
print("animals:",animals)
print("cat in animals:",'cat' in animals)
letters = set('your mother was a hamster')
print("letters of 'your mother was a hamster':",letters)
alphaLetters = list(letters)
alphaLetters.sort()
print("letters alphabetically:",alphaLetters)
frogs=set('french')
print("letters shared with 'french':",letters & frogs)
print("letters NOT in 'french':",letters - frogs)
print("inside letters or 'french':",letters | frogs)
print("letters XOR french:",letters ^ frogs)
comprehension={q for q in frogs if q not in 'cyphersetremoval'}
print("secret cypher removed letters:",comprehension)
debts = {"Fiola":4000,"Jimmy the Knee":9999,"Criscuolo":500}
print("Mob debts:",debts)
print("debtors:",sorted(debts))
del(debts['Fiola'])
print("Fiola taken care of:",debts)
#debts = {x:debts[x]*2 for x in debts}
debts = {x:y*2 for x,y in debts.items()}	#equivalent
print("Nobody paid up, interest charged:",debts)
debts = dict(theshop=200000,themechanic=300000)
print("all is forgiven, they have found us bigger fish to fry:",debts)
f=lambda x: x[0]+x[1]
print("similar in lists:",f(list(enumerate(letters))))
questions = ['your name','your quest','the airspeed velocity of an unladen swallow']
robin = ['robin','to seek the grail',"I don't know that!"]
arthur = ['arthur','to seek the grail','what do you mean, african or european?']
print("\nbravely bold sir robin moved forth to answer questions")
for q,a in zip(questions, robin):
	qastr='	What is {0}?  {1}'.format(q,a)
	print(qastr)
print("Then came arthur, king of the britons")
for q,a in zip(questions, arthur):
	qastr='	What is {0}?  {1}'.format(q,a)
	q="yourmom"	#no effect on the already made string
	print(qastr)
