from sys import argv

# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

script, first, second, third, fourth = argv

fifth = raw_input("Fifth:")
sixth = raw_input("Sixth:")

print "Script:", script
print "First:", first
print "Second:", second
print "Third:", third
print "Fourth:", fourth
print "Fifth: %s" % (fifth)
print "Sixth: %s" % (sixth)
