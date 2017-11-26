# 3.1 Names:

names = ['aby', 'abyss', 'sanju', 'kiddo']

# printing each name separatly
print(names[0])
print(names[1])
print(names[2])
print(names[3])


# 3.2 greeting

message = 'Hello, ' + names[0] + '.'
print(message)
message = 'Hello, ' + names[1] + '.'
print(message)
message = 'Hello, ' + names[2] + '.'
print(message)
message = 'Hello, ' + names[3] + '.'
print(message)


# 3.3 your own list

my_likes = ['car', 'bike', 'plane']

for i in my_likes:
    print('I would like to own a ' + i + '.')


# 3.4 Guest List

guests = ['aby', 'abyss', 'kiddo']
# prints the persons invited
for i in guests:
    print("Hey, " + i.title() + " please come to the party.")


# 3.5 Changing guests list

# abyss cant make it
print(guests.pop(1).title() + " cant make it\n")

# adding new member
guests.insert(1, 'sanju')
# printing the persons invited
for i in guests:
    print("Hey, " + i.title() + " please come to the party.")


# 3.6 More Guests

print("Found a bigger table\n")

# adding more members
guests.insert(0, 'aish')
guests.insert(int(len(guests) / 2), 'shy')
guests.insert(len(guests), 'saji')

# printing invites

for i in guests:
    print("Hey, " + i.title() + " please come to the party.")


# 3.7 Shrinking Guest List

print("I can invite only two people to the party")
print(guests)
while len(guests) > 2:
	pop_guest = guests.pop()
	print("Sorry %s I won't be able to invite you" % pop_guest.title())

for i in guests:
	print("Hey, ", i.title(), "please come to the party.")

for i in range(len(guests)):
	del guests[0]

print(guests)
