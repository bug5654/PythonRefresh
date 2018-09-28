import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")	#use this for everyone else
group = parser.add_mutually_exclusive_group()	#use group.add_argument for mutually exclusives
group.add_argument("-v", "--verbose", action="count", default=0)
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose==1:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbose>1:
	i=0
	while i < args.y:
		print(args.x,end=" ")
		if (i < args.y-1):
			print("*",end=" ")
		i+=1
	print("=",answer)
else:
    print("{}^{} == {}".format(args.x, args.y, answer))