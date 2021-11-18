#!/usr/bin/env python3

import logging
from logging import FileHandler
from logging import Formatter


def logs():


   LOG_PATH='/tmp/akamai_papi.log'
   LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

   logger = logging.getLogger('debug')
   logger.setLevel(logging.DEBUG)
   logger_file_handler = FileHandler(LOG_PATH)
   logger_file_handler.setLevel(logging.DEBUG)
   logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
   logger.addHandler(logger_file_handler)


    return logger
