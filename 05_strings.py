# %%
# strings are immutable, methods return new instance
my_str = "Hi, i am gab"

my_multiline = """ this is \
my mutliline \
code
"""

print(my_multiline)
# %%
# Methods

print(my_str.startswith("H"))
print(my_str.find(','))  # find first appearence of a char or word
print(my_str.count('i'))
print(my_str.replace('i', "#"))
print(my_str.split()) # default delimites is space

# %%
# Placeholder

name = "Gab"
surname = "Kos"
text = "My name is %s" % name

text = "My name is {} and {}".format(name, surname)

text = f"My name is {name} and {surname}"
print(text)

# %%
