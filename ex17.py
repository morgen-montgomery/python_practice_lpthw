from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file).read()

print "The input file is %d bytes long" % len(in_file)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print "Alright, all done."

in_file.close()

# SD
# 1- go back and look up some 'features' you could change
# 4- because it is good practice to close a file you have opened up?
