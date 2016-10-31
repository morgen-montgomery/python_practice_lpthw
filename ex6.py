# set var 'x' to a string with a Python format character
x = "There are %d types of people." % 10

# set var 'binary' to string 'binary'
binary = "binary"

# set var 'do_not' to string 'don't
do_not = "don't"

# set var 'y' to a string with 2 Python format characters
# string in a string
y = "Those who know %s and those who %s." % (binary, do_not)

# print value of 'x'
print x

# print value of 'y'
print y

# print string with a string inside
# string in a string
print "I said: %r." % x

# print string with a string inside
# string in a string
print "I also said: '%s'." % y

# set var 'hilarious' to False
hilarious = False

# set var 'joke_evaluation' to a string with a Python format character
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation with hilarious answer
print joke_evaluation % hilarious

# set var 'w' equal to a string
w = "This is the left side of..."

# set var 'e' equal to another string
e = "a string with a right side."

# print a concatenation of two strings
print w + e
