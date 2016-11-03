# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print num

# # convert while-loop to a callable function with:
# # a constraint variable
# # increment prompt
# def loop_function_practice(x):
#     i = 0
#     numbers = []
#
#     increment_by = int(raw_input("How much would you like to incrememnt by? "))
#
#     while i < x:
#         print "At the top i is %d" % i
#         numbers.append(i)
#
#         i = i + increment_by
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i
#
#     print "The numbers: "
#
#     for num in numbers:
#         print num
#
# loop_function_practice(100)
#

# use for-loop and range:
def loop_function_practice():
    number_list = []
    r = int(raw_input("Yo, what's your end number? "))

    for num in range(0, r):
        print "Here is the next value: %d" % num
        number_list.append(num)

loop_function_practice()

# SD
# am I doing the "Convert this while-loop to a function that
# you can call, and replace 6 in the test (i < 6) with a
# variable." part correctly?
