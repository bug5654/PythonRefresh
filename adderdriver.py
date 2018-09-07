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
		valu=int(valu)
		loop=False
	except:
		print("please input an integer")
		continue
simplecalc2 = adder(val=valu)
simplecalc2.add(42)
print("after manipulation the number is: %f" % simplecalc2.getValue())