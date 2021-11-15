#!/usr/bin/env python3

from urllib.parse import urljoin

class group:
  
    def get(self,connection,baseurl):
        return connection.get(urljoin(baseurl, '/papi/v1/groups'))
  
   
