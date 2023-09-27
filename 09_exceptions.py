# %%
# Raise an exception

if 2 > 0:
    raise Exception("This is a message for exception")

# %%
# assert will throw an assertion error

assert 5 > 10 , "5 IS LESS THAT 10"

print("Will not executed")

# %%
# Handle exceptions

try:
    x = 5/0
except Exception as e:
    print(e)
else:
    print("After try code when all its ok")
finally:
    print("Last in all cases")
# %%
# Custom exceptions

class CustomException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value   = value
    
try:
    raise CustomException("This is a custom exception",100)
except CustomException as e:
    print(e.message, e.value)


# %%
