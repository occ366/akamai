#!/usr/bin/env python3

from urllib.parse import urljoin
import re

from logger import get_module_logger
logger = get_module_logger('debug')

class cpcode:

    def  __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/cpcodes?groupId={}&contractId={}".format(groupId,contractId)


    def reader(self,response):
        """get all cpcodes in readly format"""
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
        except:
            logger.error('cpcode.reader(), Error on values') 

    def getAll(self,connection,baseurl,json=True):
        """get all propieties in json format"""
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=connection.get(urljoin(baseurl, self.__papiurl),headers = headers)

        if response.status_code != 200:
             logger.error('cpcode.getAll(): Error code {} on call'.format(response.status_code))
             logger.error(response.json())

        else:
            self.__allcpcodes=response.json()
            if json:
                """get all propieties in json format"""
                return response.json()

            else:
                self.reader(response)


    def getCPcode(self,connection,baseurl,cpcodeId,json=True):
        """get data for one propiety in json format"""
        papiurl = '/papi/v1/cpcodes/{}?groupId={}&contractId={}'.format(cpcodeId,self.__groupId,self.__contractId)
        headers = { 'PAPI-Use-Prefixes' : 'true' }

        response=connection.get(urljoin(baseurl, papiurl),headers=headers)

        if response.status_code != 200:
            logger.error('cpcode.getCPcode: Error, code {} on call'.format(response.status_code))
            logger.error(response.json())

        else:
            if json:
                return response.json()

            else:
                self.reader(response)


    def createCPcode(self,connection,baseurl,productId,cpcodeName,json=True):

        cpcodeID = self.checkIfExist(cpcodeName) 

        if cpcodeID:

            logger.info('cpcode.createCPcode(): cpcode for {} already exists {}'.format(cpcodeName,cpcodeID))
            return cpcodeID


        else:

            """create a new CPcode"""
            send_data = """
                          {
                              "productId": "%s",
                              "cpcodeName": "%s"
                          }""" % (productId,cpcodeName)

            headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
            response = connection.post(urljoin(baseurl, self.__papiurl),data=send_data,headers=headers)

            if response.status_code != 201:
                logging.error('cpcode.createCPcode(): Error, code {} on call'.format(response.status_code))
                logging.error(response.json())

            else:
                cpcodeID = re.search(r'cpc_\d+', response.json()['cpcodeLink'])[0]
                logger.info('cpcode.createCPcode(): create new cpcode, code {} on call'.format(cpcodeID))
                return  cpcodeID


    def checkIfExist(self,cpcodeName):
        """ check the cpcname if exit return de cpcodeId """
        rback = False

        for cpcode in self.__allcpcodes['cpcodes']['items']:
            if cpcodeName in cpcode['cpcodeName']:
               rback = cpcode['cpcodeId']

        return rback

