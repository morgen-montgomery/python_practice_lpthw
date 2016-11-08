things = "1 2 3 4 5 6 7 8 9 10 Jack Queen King Ace"

hearts = things.split(' ')
print "Hearts = %s" % hearts
diamonds = things.split(' ')
print "Diamonds = %s" % diamonds
spades = things.split(' ')
print "Spades = %s" % spades
clubs = things.split(' ')
print "Clubs = %s" % clubs

# add cards to same list
# shuffle cards
# prompt for how many players will be playing (between 2-5)
# deal 7 cards to X number of players
# assign remaining cards into fish-wish well
# player1 =
# player2 =
# player3 =
# player4 =
# fishing_wishing_well =

# pick a random player to start
# prompt ^this^ player to ask another -player for a -card
#   if asked player has card:
#        remove card from hand of both players
#        add a point to asking player
#        repeat from prompt
#   else
#        say no luck, go fish
#           if you fish your wish
#               remove card from hand of active player and fishing_wishing_well
#               add a point to asking player
#               repeat from prompt
#           else move to the next player
# go to next player in circle (establish order)
# while all players have at least one card, continue game
# once any player has no more card, game is over
# add players points up
# print "player_" is the winner with "numbre" points!
