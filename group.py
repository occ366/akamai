#!/usr/bin/env python3

from urllib.parse import urljoin


LOG_PATH='/tmp/akamai_papi.log'
LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)
logger_file_handler = FileHandler(LOG_PATH)
logger_file_handler.setLevel(logging.DEBUG)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler



class group:

    def get(self,connection,baseurl):

        response = connection.get(urljoin(baseurl, '/papi/v1/groups'))
        if response.status_code != 200:
            logger.error('gruop.get(): Error, code {}, on call'.format(response.status_code))

            logger.error(rseponse.json())
        else:

            return response.json()


