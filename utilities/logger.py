import inspect
import logging


def loggen():

    name = inspect.stack()[1][3]
    logger = logging.getLogger(name)

    file = logging.FileHandler("G:\\SnehaLambdatest\\Logs\\Lambda.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file.setFormatter(formatter)
    logger.addHandler(file)
    logger.setLevel(logging.INFO)
    return logger
