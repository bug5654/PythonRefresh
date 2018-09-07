print("String analysis program")
stringVar = "  Greetings Program!  "
stringVarReset = stringVar

print("string in question: '" + stringVar + "'")
print( "number of 'e's: " + str(stringVar.count("e")) )
print( "position of 'P' " + str(stringVar.find('P')) )
#confirmed: 0-based string position (C-style)
print( "lowercase: " + stringVar.lower() )
print( "uppercase: " + stringVar.upper() )
print( "e->q: " + stringVar.replace('e','q') )
stringVar = stringVarReset
print( "strip whitespace: " + stringVar.strip() )