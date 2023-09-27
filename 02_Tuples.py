# Collection of data that is ordered, immutable, allows duplicates

# %%
my_tpl = (1,2,3)
my_single_item_tlp = ("aaa",)
tlp_from_lst = tuple([1,2,3,3,3,4,5])
print(type(tlp_from_lst))
print([3])

# %%
# Methods

print(len(tlp_from_lst))
print(tlp_from_lst.index(3)) # index of value in first appearance
print(tlp_from_lst.count(3)) # count the 3s in tuple
# %%
# Unpack, the elements must match
tlp_details = ("Gab", 33, "Green", True)
name, age, color, isgood = tlp_details
print (name, age, color)

name, *rest, isgood_flag = tlp_details
print(rest)
# %%
