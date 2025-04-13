import logging
from functools import wraps

# logging configuration with a constumized format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_calls(func):
    """returns a message with the function call"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function called: {func.__name__} with Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Returned: {result}")
        return result
    return wrapper
