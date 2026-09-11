import logging
import os

os.makedirs('login', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('login/app1.log'),
        logging.StreamHandler()
    ],
    force=True
)


logger = logging.getLogger('Arithmetic App')


def add(a,b):
    result = a+b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result

def subtraction(a,b):
    result = a-b
    logger.debug(f'subtracting {a} - {b} = {result}')
    return result

def multiplication(a,b):
    result = a*b
    logger.debug(f'multiplication {a} * {b} = {result}')
    return result

def divisition(a,b):
    try:
        result = a/b
        logger.debug(f'Devesition is {a} / {b} = {result}')
        return result
    except ZeroDivisionError as ex:
        logger.debug(f"{ex}")
        return None

add(2,3)

subtraction(3,2)

multiplication(3,2)

divisition(6,0)