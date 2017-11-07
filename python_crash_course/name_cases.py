# Personal message
name = "you"
print("Hello " + name + ", would you like to learn Python today?")

# Name Cases
name = "aby abyss"
print("With lower(): " + name.lower())
print("With upper(): " + name.upper())
print("With title(): " + name.title())

# Famous Quote && Famous Quote 2
name = 'albert einstein'
quote = '"A person who never made a mistake never tried anything new."'
print(name.title() + " once said, " + quote)


# Stripping Names
name = '\t\nAbyss\t\n'
print('Hello, ' + name + ' sup?')

print('Hello, ' + name.rstrip() + ' sup?')
print('Hello, ' + name.lstrip() + ' sup?')
print('Hello, ' + name.strip() + ' sup?')
