listsample = [1,5,2,'a','a','q', False]

print("starting: " + str(listsample) )
listsample.append(True)
print("append: " + str(listsample) )
listsample.count('a')
print("count: " + str(listsample) )
listsample.index('q')
print("index q: " + str(listsample) )
listsample.insert(2,'x')
print("inserted x: " + str(listsample) )
listsample.pop()
print("after a pop: " + str(listsample) )
listsample.remove('x')
print("x removed: " + str(listsample) )
listsample.reverse()
print("after a reverse: " + str(listsample) )

comprable = [2,5,16,2,4]
print("numerical list: " + str(comprable) )
comprable.sort()
print("after sorting: " + str(comprable) )