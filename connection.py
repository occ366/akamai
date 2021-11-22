#!/usr/bin/env python3

import resquests
import from urllib.parse import urljoin
from akamai.edgegrid import EdgeGridAuth, EdgeRc

from requests import ConnectionError
from requests import HTTPError
from requests import Timeout


import logging
logger = logging.getLogger(__name__)


TIME_OUT = 10


class connection:

    def __init__ (self, path_credential,secction):

        self.__secction = secction
        self.__edgerc = EdgeRc(path_credential)
        self.__baseurl = 'https://%s' % edgerc.get(section, 'host')
        self.__connect = requests.Session()
        self.__connect.auth = EdgeGridAuth.from_edgerc(edgerc, self.__section)


    def get(self, url, headers):

        try:
            response = connect.get(urljoin(self.__baseurl, url))
            response.raise_for_status()
            logger.info('connection.get(): Get json for: {}'.format(url))
            return response

         except ConnectionError:
             logger.info('connection.get(): Connection error. Retrying...')
             sleep(TIME_OUT)

         except Timeout:
             logger.info(' connection.get(): Timeout. Retrying...')
             sleep(TIME_OUT)

         except HTTPError:
             logger.info('connection.get(): HTTP error. Code {}'.format(response.status_code))
             logger.info('connection.get(): Response: {}'.format(response.json()))

         except:
             logger.info('connection.get(): Unexpected error..')


    def put(self, url, send_data ,headers):

        try:
            response = connect.put(urljoin(self.__baseurl, url),data=send_data,headers = headers)
            response.raise_for_status()
            logger.info('connection.put(): Get json for: {}'.format(url))
            return response

         except ConnectionError:
             logger.info('connection.put(): Connection error. Retrying...')
             sleep(TIME_OUT)

         except Timeout:
             logger.info(' connection.put(): Timeout. Retrying...')
             sleep(TIME_OUT)

         except HTTPError:
             logger.info('connection.put(): HTTP error, Code {}'.format(response.status_code))
             logger.info('connection.put(): Response: {}'.format(response.json()))

         except:
             logger.info('connection.put(): Unexpected error..')


    def path(self, url, send_data ,headers):

        try:
            response = connect.path(urljoin(self.__baseurl, url),data=send_data,headers = headers)
            response.raise_for_status()
            logger.info('connection.path(): Path json for: {}'.format(url))
            return response

         except ConnectionError:
             logger.info('connection.path(): Connection error. Retrying...')
             sleep(TIME_OUT)

         except Timeout:
             logger.info(' connection.path(): Timeout. Retrying...')
             sleep(TIME_OUT)

         except HTTPError:
             logger.info('connection.path(): HTTP error, Code {}'.format(response.status_code))
             logger.info('connection.path(): Response: {}'.format(response.json()))

         except:
             logger.info('connection.path(): Unexpected error..')


    def post(self, url, send_data ,headers):

        try:
            response = connect.post(urljoin(self.__baseurl, url),data=send_data,headers = headers)
            response.raise_for_status()
            logger.info('connection.put(): Get json for: {}'.format(url))
            return response

         except ConnectionError:
             logger.info('connection.put(): Connection error. Retrying...')
             sleep(TIME_OUT)

         except Timeout:
             logger.info(' connection.put(): Timeout. Retrying...')
             sleep(TIME_OUT)

         except HTTPError:
             logger.info('connection.put(): HTTP error, Code {}'.format(response.status_code))
             logger.info('connection.put(): Response: {}'.format(response.json()))

         except:
             logger.info('connection.put(): Unexpected error..')

