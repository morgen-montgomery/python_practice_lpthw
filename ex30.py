# sets var 'people' to an int value
people = 30
# sets var 'cars' to an int value
cars = 40
# sets var 'trucks' to an int value
trucks = 15

# if cars is greater than people print "We should take the cars"
if cars > people:
    print "We should take the cars."
# else if cards is less than people print "We should not take the cars"
elif cards < people:
    print "We should not take the cars."
# else print "We can't decide"
else:
    print "We can't decide."

# if trucks is greater than cars print "That's too many trucks"
if trucks > cars:
    print "That's too many trucks."
# else if trucks is less than cars print "Maybe we could take the trucks"
elif trucks < cars:
    print "Maybe we could take the trucks."
# else print "We still cant decide."
else:
    print "We still can't decide."

# if people is greater than trucks and trucks is greater than people print
# "Alright, let's just take the trucks"
if people > trucks and trucks > people:
    print "Alright, let's just take the trucks."
# else print "Fine, let's stay home then"
else:
    print "Fine, let's stay home then."
