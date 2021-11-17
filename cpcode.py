#!/usr/bin/env python3

from urllib.parse import urljoin

class cpcode:

    def  __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/cpcodes?groupId={}&contractId={}".format(groupId,contractId)
        self.__allcpcodes = {}

    def reader(self,response):
        """get all propieties in readly format"""
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

    def getAll(self,connection,baseurl,json=True):
        """get all propieties in json format"""
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=connection.get(urljoin(baseurl, self.__papiurl),headers = headers)

        if response.status_code != 200:
             print ('Error {}'.format(response.status_code))
             print(response.json())

        else:
            self:__allcpcode=response.json()
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
            print ('Error {}'.format(response.status_code))
            print (response.json())

        else:
            if json:
                return response.json()

            else:
                self.reader(response)


    def createCPcode(self,connection,baseurl,productId,cpcodeName,json=True):
        
        cpcodeID = self.checkIfExist(self,cpcodeName) 

        if cpcodeID:

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
                print ('Error {}'.format(response.status_code))
                print(response.json())

            else:
                return response.json()


    def checkIfExist(self,cpcodeName):
        """ check the cpcname if exit return de cpcodeId """
        rback = False

        for cpcode in self.__allcpcodes['cpcodes']['items']:
            if name in cpcode['cpcodeName']:
               rback = cpcode['cpcodeId']

        return rback

