# Small inline function that is defined without name
# %%
from functools import reduce
# %%
# lambda arguments: expression

func = lambda x: x-1

print(func(9))
# %%
# map: map a function on a collection

l = [1,2,3,4,5,6]

b = map(lambda x: x*2, l)
# same as

c = [x*2 for x in l]
print(list(b))
# %%
# filter: apply a function that return true/false and return all the rows that return true

f = filter(lambda x: x< 3, l)
print(list(f))
# %%
#reduce: apply a function and return a single value
# the function should always has two arguments, the one is the current value and the other is the aggregated until current

prod = reduce(lambda x,y: x+y ,l)
print(prod)
# %%
