# %%
# Parameters: are the inputs declared in a function
# Arguments:  are the input send to function when calling it

# parameter
def print_name(name):
    print(name)

# argument
print_name("Gab")

# %%
# Positional vs keywor arguments: 
# Positional: pass arguments in the same order of parameters
# Keyword: pass the arguments by name of parameters, can be in any order

# when using default must be all in the end
def print_params(a,b,c=99):
    print(a,b,c)

# Positional
print_params(1,2,3)

# Keyword
print_params(b=2,a=1,c=3)

# I can mix arguments but after a keyword argument cannot use positional
print_params(1,b=1,c=3)

# use default
print_params(1,2)
# %%
# Variable length params

# args is a tuple
# kwargs is dict
def print_dynamic_params(*args,**kwargs):
    print(args)

    for i in args:
        print(i)

    for k,v in kwargs.items():
        print(k,v)

print_dynamic_params('a','b','c', x='xx', y='yy')
# %%
# Unpack arguments

def foo(a,b,c):
    print(a,b,c)

my_args = [1,2,3]

# unpack the list/tuple to arguments, length must match the number of params
foo(*my_args)
# %%
# local vs global variable


## from functions we can refer the variables in the main script
# But when we assign a value it creates a local variable
# If we want to modify the global variable we have to specify it with the global keyword
def foo():
    global my_global 
    x = my_global
    my_global = 10
    print(x, my_global)
my_global = 10


foo()
print(my_global)
