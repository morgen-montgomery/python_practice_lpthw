# import a module that brings us the argv feature
from sys import argv

# set a number of argvs to argv
script, filename = argv

# open the file with the filename we have passed from the command line
txt = open(filename)


# print name of file, and text in file
print "Here's your file %r:" % filename
print txt.read()

# this closes the file
txt.close()

# # this makes you type the filename again, into a prompt this time
# print "Type the filename again:"
# file_again = raw_input("> ")
#
# # this opens the file again
# txt_again = open(file_again)
#
# # this reads the file... again
# print txt_again.read()
## this closes the file
# txt_again.close()

# SD
# 6- how do I open from within Python prompt?
