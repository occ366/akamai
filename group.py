#!/usr/bin/env python3

from urllib.parse import urljoin

class group:
    def get(self,connection,baseurl):
        response = connection.get(urljoin(baseurl, '/papi/v1/groups'))
        if response.status_code != 200:
            logger.error('gruop.get(): Error, code {}, on call'.format(response.status_code))
            logger.error(rseponse.json())
        else:
            return response.json()


