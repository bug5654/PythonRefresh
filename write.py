f = open("file.txt", "w")
f.close()		#if file.txt existed, it's empty now

f = open("file.txt", "w")
f.write("Llorem ipsum")
f.write("neque porro quisquam est qui dolorem")
f.write("ipsum quia dolor sit amet, consectetur, adipisci velit")
f.close()

f = open("file.txt", "r")
print(f.read())