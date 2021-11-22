#!/usr/bin/env python3

from urllib.parse import urljoin

import logging
from logging import FileHandler
from logging import Formatter


LOG_PATH='/tmp/akamai_papi.log'
LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)
logger_file_handler = FileHandler(LOG_PATH)
logger_file_handler.setLevel(logging.DEBUG)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler)


class cpcode:

    def  __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/cpcodes?groupId={}&contractId={}".format(groupId,contractId)
        self.__allcpcodes = {}

    def reader(self,response):
        """get all propieties in readly format"""
        try:
            for cpcode in response.json()['cpcodes']['items']:
                 print("---------------------------\n \
                        cpcodeId {}\n \
                        cpcodeName : {}\n \
                        productIds : {}\n \
                        createdDate : {}\n ".format(cpcode['cpcodeId'], \
                                                    cpcode['cpcodeName'], \
                                                    cpcode['productIds'], \
                                                    cpcode['createdDate'])
                      )
        except e:
            logger.error('cpcode.reader(), Error on values') 

    def getAll(self,connection,json=True):
        """get all propieties in json format"""
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=connection.get(self.__papiurl,headers = headers)

        self.__allcpcode=response.json()

        if json:
            """get all propieties in json format"""
            return response.json()

        else:
            self.reader(response)


    def getCPcode(self,connection,cpcodeId,json=True):
        """get data for one propiety in json format"""
        papiurl = '/papi/v1/cpcodes/{}?groupId={}&contractId={}'.format(cpcodeId,self.__groupId,self.__contractId)
        headers = { 'PAPI-Use-Prefixes' : 'true' }

        response=connection.get(urljoin(baseurl, papiurl),headers=headers)

        if json:
            return response.json()
        else:
            self.reader(response)


    def createCPcode(self,connection,baseurl,productId,cpcodeName,json=True):

        cpcodeID = self.checkIfExist(self,cpcodeName) 

        if cpcodeID:

            return cpcodeID
            logger.info('cpcode.createCPcode(): cpcode for {} already exists {}'.format(cpcodeName,cpcodeID))

        else:

            """create a new CPcode"""
            send_data = """{"productId": "%s","cpcodeName": "%s"}""" % (productId,cpcodeName)

            headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
            response = connection.put(self.__papiurl),data=send_data,headers=headers)

            return response.json()


    def checkIfExist(self,cpcodeName):
        """ check the cpcname if exit return de cpcodeId """
        rback = False

        for cpcode in self.__allcpcodes['cpcodes']['items']:
            if name in cpcode['cpcodeName']:
               rback = cpcode['cpcodeId']

        return rback

