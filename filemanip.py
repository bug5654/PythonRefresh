f = open("./text.txt", "r")

print( f.read(1) )
print( f.readline() )
print( f.readline() )
print( f.read() )
f.close()

mylist = []
f = open("text.txt", "r")
for line in f:
	mylist.append(line)
print(mylist)