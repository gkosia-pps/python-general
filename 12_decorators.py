# %%
# Decorators: extend the behaivior of the method without change it
import functools
from typing import Any

# %%
# Function decorators
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def print_name():
    print("Gab")

@start_end_decorator
def print_name_zac(name):
    print(name)
    return -99

print_name = start_end_decorator(print_name)
print_name()
print(print_name_zac("Zacc"))
print(help(print_name_zac))


# %%
#Class decorators: receive in init a function, extend the functionality by impement the __call__
#Used to keep in vthe decorator the state of the function

class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds):
        self.num_calls+=1
        print(f"Executed {self.num_calls} times")
        return self.func(*args, **kwds)
    
@CountCalls
def say_hello():
    print("Hello")    


say_hello()
say_hello()



# %%
