from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "The first variable is: ", first
print "The second variable is: ", second
print "The third variable is: ", third
y = raw_input("Enter y value: ")
x = raw_input('Enter x value')

print "You've entered point (x,y) = (%r,%r)" % (x, y)