from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %r to %r" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL+C to exit"
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "allrigth, all done"
in_file.close()
out_file.close()


