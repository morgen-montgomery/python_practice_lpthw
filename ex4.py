# set var 'car' equal to 100
cars = 100

# set var 'space_in_a_car' equal to 4.0
space_in_a_car = 4.0

# set var 'drivers' equal to 30
drivers = 30

# set var 'passengers' equal to 90
passengers = 90

# set var 'cars_not_driven' equal to values of cars minus value of drivers
cars_not_driven = cars - drivers

# set var 'cars_driven' equal to value of drivers
cars_driven = drivers

# set var 'carpool_capacity' equal to value of cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# set var 'average_passengers_per_car' equal to value of passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers avaialble."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
