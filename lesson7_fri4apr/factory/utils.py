import logging



def is_called(func):
    
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} is called")
        res = func(*args, **kwargs)
        logging.info(f"{func.__name__}is executed with args:{args} and kwargs: {kwargs}")
        return res
    return wrapper
