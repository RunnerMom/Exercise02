#LPTHW ex18
#Day 3 of hackbright

#Names, Variables, Code, Functions


#this one is like your scripts with argv?

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (args[0], args[1])

# ok, that * args is actually pointless, we cna just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no args
def print_none():
	print "I got nothin"
#
#def print_all(*args):
#	for arg in args
#		print arg

		###calling fuctions now ###

print_two("Gowri", "Grewal")
print_two_again("Gowri","Rao")

#print_two("Gowri", "Rao", "Grewal")
print_one("First!")
print_none()

#print_two_again("Calvin", "Rao", "Grewal")

