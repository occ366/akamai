#!/usr/bin/env python3

from urllib.parse import urljoin


class rules:

    def __init__(self,propietyId,versionId,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__versionId=versionId
        self.__papiurl="/papi/v1/properties/{}/versions/{}/rules?groupId={}&contractId={}".format(propietyId,versionId,groupId,contractId)


    def getAll(self,connection,baseurl,json=True):

        response=connection.get(urljoin(baseurl, self.__papiurl))

        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
            print(response.json())
        else:
            if json:
                """get all rules in json format"""
                return response.json()

            else:
                """get all rules in readly format"""
                reader(response)

    def createSetRules(self,connection,baseurl,sent_data):
        """create a set of new rules """

        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }

        result = sesson.put(urljoin(baseurl, self.__papiurl),data=sent_data,headers=headers)

        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
            print(response.json())

        else:
            return response.json()

