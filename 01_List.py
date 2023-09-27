#https://www.youtube.com/watch?v=HGOBQPFzWKo

# Collection of ordered, mutable and allows duplicates
# allows different data types

# %%
my_lst = ["gab", "nick", "zak", "zak", 1, True]

# init an empty list
my_empty_list = list()

print(my_lst)

# refer by index 
print(my_lst[0])  # the first
print(my_lst[-1]) # the last

# get the size
print(len(my_lst)) 

# %%
# iter over list
for i in my_lst:
    print(i)

# %%
# check if value exists in list
if "gab" in my_lst:
    print("gab is in the list")

# %%
# Methods

my_lst.append("aaaa")     # add to the end
my_lst.insert(2,"second") # add to specific place
my_lst.pop()              # remove and return the last item
my_lst.remove(True)       # remove a value, throws error if not exists
my_lst.reverse()
my_lst.sort()             # sort in place
my_lst_sorted = sorted(my_lst) # do not sort inplace but sort and assign it to new var
print(my_lst)

concat_lst = my_lst + my_lst_sorted
print(concat_lst)

# %%
# Slicing[start:stop:step]

print(concat_lst[2:5]) # from 2 until 4
print(concat_lst[:5])  # from beginning until 4
print(concat_lst[5:])  # from 5 until end
print(concat_lst[::-1]) # reverse the list

# %%
# list comprehension
# iterate on the list based on a condition and produce a new list

my_numbers = [1,2,3,4,5,6,7]

print([i*2 if i%2 == 0 else -1 for i in my_numbers])

