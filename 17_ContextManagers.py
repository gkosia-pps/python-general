# %%
# Context manager is use to alocate and release resources 
with open('logs.log', 'r') as logfile:
    print(logfile.read())
# %%
# Custom contaxrt manager
# Have to implement enter, exit methods

class CustomContextManager:
    def __init__(self, file) -> None:
        print("__init__")
        
    def __enter__(self):
        '''
            Open file logic
        '''
        print("__enter__")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''
            Close file logic
        '''
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
        print("__exit__")
        

# exc_type, exc_value, exc_traceback will be passed as None
# In case of exception will be filled and we can handle it in __exit__ and return true
# If we dont handle it the with will call the __exit__ but also will raise an exception
with CustomContextManager("file.txt") as file:
    print("Process file")

print("After context manager")
# %%
