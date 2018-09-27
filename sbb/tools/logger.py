# https://docs.python.org/3.6/howto/logging-cookbook.html
# TODO: Include Process and ThreadID and Caller Identity
# https://stackoverflow.com/questions/3926017/log-message-style-guide
import logging
from pathlib import Path
# logger
logger = logging.getLogger('APIlogger')
logger.setLevel(logging.INFO)

# file handler
# TODO: test if this works on $HOME
log_dir = Path("~/train-sbb-challenge").expanduser()
if not log_dir.is_dir():
    log_dir = Path("~/dev/projs/train-sbb-challenge").expanduser()
    assert log_dir.is_dir(), str(log_dir)

# ah = str(log_dir) + '/logs/API.log'
# import pdb
# pdb.set_trace()
fh = logging.FileHandler(str(log_dir) + '/logs/API.log')
fh.setLevel(logging.DEBUG)

# console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format and set https://docs.python.org/3/howto/logging.html#a-simple-example
# logging.basicConfig(
#     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
formatter = logging.Formatter(
    '%(name)s - %(threadName)s: #%(levelname)s - %(message)s')
ch.setFormatter(formatter)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(threadName)s: #%(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# TODO: Finding better ways of starting and finishing loggers
# loger.DEBUG("### Log Started ###")