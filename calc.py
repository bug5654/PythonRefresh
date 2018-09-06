print("The output will make no sense to you without looking at the source because the print statements would get very numerous")

a = "0"
b = 2
print( int(a) + b )		#cast a to an int before printing to avoid overloaded '+'

#the rest of the basic operators copypasta'd
print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (3 % 2)
print (3 ** 4) # 3 to the fourth power
print (4 // 3) #floor division

#ifchecks
if b > 3 :
	print(" b > 3...and we have a problem")
b+=b
print(b)

if b>3 :
	print("b > 3 correctly")

#for loop
for q in range(2,4):		#[min,max) apparently in setbuilder notation
	print(q)

#while loop
r = 0
while r<5:
	print(r)
	r+=1		#r++ wrong language
#there is no conflict...I mean do-while