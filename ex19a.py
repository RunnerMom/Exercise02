#LPTHW ex19
#create your own function and run it 10 ways

def circumference(radius):
	print "The circumference of a circle with radius %r is" % radius, 2*3.14159*radius

print "fixed radius"
circumference(4)

print "radius is a math expression"
circumference(50+4/7)

print "radius is a variable"
size_of_soccer_ball=18
circumference(size_of_soccer_ball)

print "radius is variables and math"
size_of_tennis_ball=5
size_of_pool=200
circumference(size_of_pool/size_of_tennis_ball)

for x in range(20):
	circumference(x)