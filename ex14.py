from sys import argv

script, user_name, time = argv
the_thing = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
print "It is %s time" % time
likes = raw_input(the_thing)

print "Where do you live %s?" % user_name
lives = raw_input(the_thing)

print "What kind of computer do you have?"
computer = raw_input(the_thing)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
