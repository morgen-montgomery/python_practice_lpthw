age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# SD
# 3- pydoc gives docs on Python modules derived from the __doc__ attribute of the object, if none is given that it will get a description fromjust above the class
# 4- pydoc searches:
# open: Open a file using the file() type, returns a file object.  This
#   is the preferred way to open a file.  See file.__doc__ for further
#   information.
# file: Open a file.  The mode can be 'r', 'w' or 'a' for reading
#   (default), writing or appending.  The file will be created if it
#    doesn't exist when opened for writing or appending; it will be
#    truncated when opened for writing.  Add a 'b' to the mode for
#    binary files. Add a '+' to the mode to allow simultaneous reading
#    and writing. If the buffering argument is given, 0 means
#    unbuffered, 1 means line buffered, and larger numbers specify the
#    buffer size.  The preferred way to open a file is with the builtin
#    open() function. Add a 'U' to mode to open the file for input with
#    universal newline support.  Any line ending in the input file will
#    be seen as a '\n' in Python.  Also, a file so opened gains the
#    attribute 'newlines'; the value for this attribute is one of None
#    (no newline read yet), '\r', '\n', '\r\n' or a tuple containing #    all the newline types seen.
#    'U' cannot be combined with 'w' or '+' mode.
#    Methods defined here:  __delattr__(...)
# os: :checkmark:
# sys: This module provides access to some objects used or maintained
#    by the interpreter and to functions that interact strongly with
#    the interpreter.
#   Dynamic objects:
#       argv -- command line arguments; argv[0] is the script pathname
#            if known
#       path -- module search path; path[0] is the script directory,
#            else ''
#       modules -- dictionary of loaded modules
#
#       displayhook -- called to show results in an interactive session
#       excepthook -- called to handle any uncaught exception other
#            than SystemExit
#           To customize printing in an interactive session or to
#            install a custom
