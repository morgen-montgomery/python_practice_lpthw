print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# SD
# 1- raw_input() will present a prompt to the user, it will get the input
#       and return the data in a string
# 2-
name = raw_input("What is your name? ")
print "Hello, %s." % name
# 3-
print "What is your favorite La Croix flavor?",
flavor = raw_input()
print "Do you like the coconut flavor?",
like = raw_input()
print "How many La Croixs do you drink a day?",
consumed_day = raw_input()
print "A week?",
consumed_week = raw_input()

print "So your favorite flavor is %s, you vote %s for coconut flavor, you drink %s a day and %s a week. Wow. you like La Croix!" % (flavor, like, consumed_day, consumed_week)

# 4- whoever answered the question, answered the prompt with "6'2"
#   instead of just 6'2

# EXTRA PRACTICE
# show menu
print (30 * '-')
print (" M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')

# get input
choice = raw_input('Enter your choice [1-3] : ')

# convert str to int type
choice = int(choice)

# take action per selected menu option
if choice == 1:
    print ("Starting backup...")
elif choice == 2:
    print ("Starting user management...")
elif choice == 3:
    print ("Rebooting the server...")
else: # default
    print ("Invalid number. Try again...")
