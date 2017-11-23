# ex16.py READING AND WRITING FILES python3
from sys import argv

script, filename = argv

print("This is what was there in %s" % filename)
read_file = open(filename)
print(read_file.read())

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

target.close()
print("This is what was there in %s" % filename)
read_file = open(filename)
print(read_file.read())

print("And finally, we close it.")
target.close()
