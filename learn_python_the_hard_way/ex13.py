# ex13.py done in python3
from sys import argv

script, first, second, third = argv
print(argv)
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# using argv in input
first_argv = input("Enter %s :" % first)
print(first_argv)