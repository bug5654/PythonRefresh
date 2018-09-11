from adderclass import *

simplecalc = adder();
simplecalc.add(2)
print(simplecalc.getValue())

loop=True
valu=None
while loop == True:
	print("Value to manipulate? ")	
	valu = input()
	try:
		valu=int(valu) #if user input a non-integer, an exception will be thrown here, going to except
		loop=False		#and not hitting here
	except:
		print("please input an integer")	#user-controlled infinite loop
		continue
simplecalc2 = adder(valu)		#instantiate with user-input value
simplecalc2.add(42)
print("after manipulation the number is: %f" % simplecalc2.getValue())
simplecalc2.passball()		#NOP
print("passball did nothing. The value is still ", simplecalc2.getValue())