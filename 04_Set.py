# Collection of unorder, mutanle, unique data
# %%
my_set = {1,2,3,4,5}
print(type(my_set))


# %%
#Methods

my_set.add(6)
my_set.remove(5) # if the value does not exists we will receive an error
my_set.discard(1000) # we will not receive an error if does not exists


# %%
# Set methods

odd = {1,3,5}
even = {2,4,6}
all = {1,2,3,4,5,6,7,8}

# all methods return a new set
# to update inplace use _update method
print(odd.union(even))
print(all.intersection(even))
print(all.difference(even))

# %%
