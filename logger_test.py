from custom_logger import logger

def addition(a: int, b:int):
    try:
        return a+b
    except TypeError:
        logger.error("test")

addition(1, "a")