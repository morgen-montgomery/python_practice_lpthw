#bring in argv module
from sys import argv

# set args
script, input_file = argv

# function to print a read version of the file
def print_all(f):
    print f.read()

# function to go to the beginning of the file
def rewind(f):
    f.seek(0)

# function to print a specific line of a file
def print_a_line(line_count, f):
    print line_count, f.readline()

# open a specific file
current_file = open(input_file)

# print the whole function for the read version of the file
print "First let's print the whole file:\n"
# do this ^
print_all(current_file)

# go back to the beginning of the file
print "Now let's rewind, kind of like a tape."
# do this ^
rewind(current_file)

# print funtion, print 3 lines
print "Let's print three lines:"
# do this ^ line 1
current_line = 1
print_a_line(current_line, current_file)
# do this ^ line 2
current_line += 1
print_a_line(current_line, current_file)
# do this ^ line 3
current_line += 1
print_a_line(current_line, current_file)


# SD
# 4- seek goes to a specific byte location within a file,
# whether explicitly or using an offset
