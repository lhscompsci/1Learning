# this is an octothorpe -- it makes a comment (line ignored by the computer)
# print("hello world")
print("Howdy, y'all")
print("I like typing this.")
print("This is fun.")

# math skills demo

print("I will not count my chickens", 2)
print("Hens: ", 25+30/6)
print("Roosters: ", 100 - 25 * 3 % 4)
print("Now I will count the eggs", 7)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(3 + 2 < 5 - 7)

# Variables and some of their powers
cars = 80
spaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = spaceInACar * cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available today.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put approximately", average_passengers_per_car, "in each car.")
