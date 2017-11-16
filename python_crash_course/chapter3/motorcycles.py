# modifying elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changing honda to ducati
motorcycles[0] = 'ducati'
print(motorcycles)


# adding new element to the list using append()
motorcycles.append('honda')   # gets added to the end of the list
print(motorcycles)


# adding element to empty list

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# adding elements using insert(<index>,item) , its has two parameters

motorcycles.insert(0, 'ducati')
print(motorcycles)


# removing elements from a list using del()

del motorcycles[0]		# we can choose the item, to remove using the index
print(motorcycles)


# removing elements from a list using pop()

popped_item = motorcycles.pop()	  # removes the last item
print(popped_item + " has been removed")
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


# removing item from desired location using pop(<index>)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_pop = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_pop.title() + ".")


# Remove item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
