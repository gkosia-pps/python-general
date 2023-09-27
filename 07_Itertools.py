# itertools: tools to handle iterators
# iterators: are objects that can be used in a for loop to iter over
# %%
from itertools import product, permutations, combinations, combinations_with_replacement,accumulate,groupby
import operator

# %%
# product
# produce the cartecian product of two lists

l1 = [1,2]
l2 = [3,4]

prod = product(l1,l2)
print(list(prod))

# %%
# permutations: return all the possible orderings

l = [1,2,3]
pr = permutations(l)
print(list(pr))

# %%
# combinations: all possible combinations with specific length
# combinations_with_replacement: adding also combiantion with its self

cm = combinations(l,2)
cm_repl = combinations_with_replacement(l,2)
print(list(cm))
print(list(cm_repl))

# %%
# accumulate: return accumulate aggregation (default is sum)
# use operator object to calculate other aggregations

acc = accumulate(l)
acc_multiply = accumulate(l, func=operator.mul)
acc_max = accumulate(l, func=max)

print(list(acc))
print(list(acc_multiply))
print(list(acc_max))

# %%
# groupby: group the items of the list based on a condition

def is_odd(v):
    return v < 2

group_obj = groupby(l, key=is_odd)

for k,v in group_obj:
    print(k, list(v))
# %%
