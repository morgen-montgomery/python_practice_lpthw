# set var 'formatter' to a string with 4 debugging formatters in it
formatter = "%r %r %r %r"

# print formatter with numbers
print formatter % (1, 2, 3, 4)

# print formatter with strings as word numbers
print formatter % ("one", "two", "three", "four")

# print formatter with True/False values
print formatter % (True, False, False, True)

# print formatter with 4 formatters
print formatter % (formatter, formatter, formatter, formatter)

# print formatter with 4 strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# if you look at how this is setup, the basic format is saying:
# print "%r %r %r %r" % (whatever is on the print line in parens)
