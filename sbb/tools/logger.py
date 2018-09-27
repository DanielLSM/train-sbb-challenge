# https://docs.python.org/3.6/howto/logging-cookbook.html
# TODO: Include Process and ThreadID and Caller Identity
# https://stackoverflow.com/questions/3926017/log-message-style-guide
import logging

# logger
logger = logging.getLogger('APIlogger')
logger.setLevel(logging.INFO)

# file handler
# fh = logging.FileHandler('/../logs/API.log')
# fh.setLevel(logging.INFO)

# console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# format and set https://docs.python.org/3/howto/logging.html#a-simple-example
# logging.basicConfig(
#     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(threadName)s: \n #%(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')
# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
# logger.addHandler(fh)
logger.addHandler(ch)
