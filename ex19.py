# setting up function cheese_and_crackers and giving it 2 arguments,
# then printing with a format character
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# passing numbers straight into the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# setting up variables and passing them into the function as the arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# using math within setting the arg values
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combinging both variables and math when setting the arg values
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# verbosity is key here
def wine_pairings(grape_type, color, food_pairing):
    print "You have %s wine." % grape_type
    print "It is %s color." % color
    print "Pair this %s wine with %s." % (grape_type, food_pairing)
    print "Fruit salad y'all!"

# lets get granular
print "Lets do this all at once, shall we?"
wine_pairings('Merlot', 'red', 'bad movies')

# set vars for function
print "Lets set the info for the function:"
wine = 'Cabernet Sauvignon'
wine_color = 'red'
food = 'sharp cheddar'

wine_pairings(wine, wine_color, food)

# no need to use math here, welcome to more suggestions for variety in running the function
