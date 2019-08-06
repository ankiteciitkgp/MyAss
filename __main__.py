import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from core.response import response

def converse(quit="quit"):
    user_input = ""
    while user_input != quit:
        user_input = quit
        try:
            user_input = input(">")
        except EOFError:
            print(user_input)
        if user_input:
            while user_input[-1] in "!.":
                user_input = user_input[:-1]
            print(response(user_input))

def initLogs(level = logging.DEBUG):
    logger = logging.getLogger('')
    logger.setLevel(level)

    handler = TimedRotatingFileHandler(filename='logs/my_assistant.log', when="midnight", interval=1)
    handler.suffix = "%d%m%Y"
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    initLogs()
    converse()