import time
import logging
from logging.handlers import TimedRotatingFileHandler


# format the log entries
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',datefmt='%Y-%m-%dT%H:%M:%S')

handler = TimedRotatingFileHandler('logfile.log', 
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

def debug(text):
    logger.debug(text)

def info(text):
    logger.info(text)

def warning(text):
    logger.warning(text)

def error(text):
    logger.error(text)

def critical(text):
    logger.critical(text)

# # generate example messages
# for i in range(2):
#     time.sleep(1)
#     logger.debug('debug message')
#     logger.info('informational message')
#     logger.warning('warning')
#     logger.error('error message')
#     logger.critical('critical failure')