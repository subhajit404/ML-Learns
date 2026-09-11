import logging
import os

# Get the folder where this Python file is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create logs folder INSIDE the login folder
log_dir = os.path.join(base_dir, 'login')
os.makedirs(log_dir, exist_ok=True)

# Log file path
log_file = os.path.join(log_dir, 'app1.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
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