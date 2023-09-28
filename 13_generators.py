# generate data one by one when requested
# much less memory instead of load all data to a list and process them one by one

# %%

def gen_countdown(num):
    print("starting")

    while num > 0:
        yield num
        num-=1

gen = gen_countdown(10)

# %%
# Use the generator
for i in gen:
    print(i)

try:
    next(gen)
except StopIteration as e:
    print("No more items")
# %%
# can be passed to any function that has as input iterator

gen = gen_countdown(5)
print(sum(gen))

gen = gen_countdown(8)
print(sorted(gen))
# %%
# Generators expressions: same as list comprehensions but with ()
# create inline generators

mygen = (i for i in range(10) if i%2==0)

print(next(mygen))
print(next(mygen))
# %%
