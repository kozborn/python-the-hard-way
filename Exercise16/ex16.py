from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that press CTRL+C (^C)."
print "If you want that press ENTER"
raw_input("?")
print "Opening the file ..."
target = open(filename, "w")
print "Truncating file, Goodbye data"
target.truncate()
print "Now I'm going to ask you for 3 lines"

line1 = raw_input("line1 > ")
line2 = raw_input("line2 > ")
line3 = raw_input("line3 > ")

print "I'm going to write this lines to file"
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally close file"
target.close()