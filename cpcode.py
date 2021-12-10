#!/usr/bin/env python3

from urllib.parse import urljoin
import re
import logging
logger = logging.getLogger(__name__)

class CPCode:
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

    def get_all(self,connection,baseurl,json=True):
        """get all propieties in json format"""
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=connection.get(urljoin(baseurl, self.__papiurl),headers = headers)
        if response.status_code != 200:
            logger.error('cpcode.get_all(): Error code {} on call'.format(response.status_code))
            logger.error(response.json())
        else:
            self.__allcpcodes=response.json()
            if json:
                return response.json()
            else:
                self.reader(response)


    def get_CPCode(self,connection,baseurl,cpcodeId,json=True):
        """get data for one propiety in json format"""
        papiurl = '/papi/v1/cpcodes/{}?groupId={}&contractId={}'.format(cpcodeId,self.__groupId,self.__contractId)
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=connection.get(urljoin(baseurl, papiurl),headers=headers)
        if response.status_code != 200:
            logger.error('CPCode.get_CPCode: Error, code {} on call'.format(response.status_code))
            logger.error(response.json())
        else:
            if json:
                return response.json()
            else:
                self.reader(response)


    def create_CPCode(self,connection,baseurl,productId,cpcodeName,json=True):
        cpcodeID = self.check_if_exist(cpcodeName) 
        if cpcodeID:
            logger.info('cpcode.create_CPCode(): cpcode for {} already exists {}'.format(cpcodeName,cpcodeID))
            return cpcodeID
        else:
            send_data = """
                          {
                              "productId": "%s",
                              "cpcodeName": "%s"
                          }""" % (productId,cpcodeName)
            headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
            response = connection.post(urljoin(baseurl, self.__papiurl),data=send_data,headers=headers)
            if response.status_code != 201:
                logging.error('CPCode.create_CPCode(): Error, code {} on call'.format(response.status_code))
                logging.error(response.json())
            else:
                cpcodeID = re.search(r'cpc_\d+', response.json()['cpcodeLink'])[0]
                logger.info('CPCode.create_CPCode(): create new cpcode, code {} on call'.format(cpcodeID))
                return  cpcodeID


    def check_if_exist(self,cpcodeName):
        """ check the cpcname if exit return de cpcodeId """
        rback = False
        for cpcode in self.__allcpcodes['cpcodes']['items']:
            if cpcodeName in cpcode['cpcodeName']:
        return rback

