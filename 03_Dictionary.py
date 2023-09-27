# Collection of key-value pairs

# %%

my_dict = {
     "name": "gab"
    ,"age": 33
    ,"color": "green"
}

print(my_dict)

my_dict2 = dict(name = "gab", age = 33, color= "green")

print(my_dict2)
# %%
# select,insert, update,delete
age = my_dict["age"]
my_dict["job"] = "data-eng" # if the key exists then is overriden

del my_dict["age"]
my_dict.pop("color") # same as delete
print(my_dict)


# %%
#Check if key exists
if "job" in my_dict:
    print("Has job")

# %%
# iterate
for k,v in my_dict.items():
    print(k,v)

# %%
# Merge dicts: The value of all existing keys will be overriden as the second dict

customer = {"name": "aaa", "age": 18}
customer_new = {"age": 33}

customer.update(customer_new)
print(customer)

# %%
