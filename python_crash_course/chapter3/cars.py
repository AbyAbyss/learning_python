# Organizing a List

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sorting a List Permanently with the sort() method
cars.sort()
print(cars)

# Sorting in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original List: ", cars)

# Using sorted()
print("\nHere is the sorted list: ", sorted(cars))

# Usinf sorted() in Reverse Alphabetical Order
print("\nHere is the Reverse-sorted list: ", sorted(cars, reverse=True))

# Original List
print("\nHere is the original List again: ", cars)


# Printing a List in Reverse Order (NOTE: not in alphabetical order)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# Using reverse()
cars.reverse()
print(cars)

# To revert back to orginal order after using reverse() using reverse() method again on the List
cars.reverse()
print(cars)


# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
# USing len()
print(len(cars))
