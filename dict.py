dict = {"orange" : 2, "apple" : -1}

print(str(dict))

print("keys are the item returned if none specified.  Listing Keys: ")
for d in dict:
	print(d)

for d in dict:
	print(d + " : " + str(dict[d]))

dict["banana"] = 4

print("after appending")
print(str(dict))