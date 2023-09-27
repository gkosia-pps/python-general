# %% 
import logging

# Levels: default over warning
'''
debug
info
warning
error
critical
'''

# by default logs are output over warning, to change that change basicConfic
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# by default logs comes from root logger
# as best practice each module shoult create its own logger and log the info with the name of the class
logger = logging.getLogger(__name__)
logger.info("aaaaa")


# %%
# Handlers
file_h = logging.FileHandler('logs.log')
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_h.setFormatter(formatter)

logger.addHandler(file_h)

logger.error("This is an error")
# %%
