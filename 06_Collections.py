# Additional functionalities on data structures
# %%
from collections import Counter
from collections import namedtuple

# %% 
# Counter
# Store in a dictionary the values as keys and the counts as values
# Can use Counter object as dictionary, provide also methods for other functionality

my_str = "aaabbbccdd"
my_counter = Counter(my_str)

print(my_counter)

print(my_counter.most_common(2))
# %%
# namedtuple
# used to create easy Structs (objects without declare the class)

# namedtuple(classname, fields in comma separeted string)
Point = namedtuple("Point", 'x,y')

pt = Point(5,6)
print(pt.x, pt.y)

# %%
