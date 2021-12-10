#!/usr/bin/env python3

from urllib.parse import urljoin

class Properties:
    def __init__(self,groupId,contractId):
        self.__groupId = groupId
        self.__contractId=contractId
        self.__papiurl="/papi/v1/properties?groupId={}&contractId={}".format(groupId,contractId)
        self.__headers = { 'PAPI-Use-Prefixes' : 'true' }

    def reader(self,connection):
        """get all properties in readly format"""
        for property in connection.json()['properties']['items']:
            print("---------------------------\n \
                   AccountId {}\n \
                   PropertyId : {}\n \
                   PropertyName : {}\n \
                   LatestVersion : {}\n \
                   StagingVersion : {}\n \
                   ProductionVersion : {}\n \
                   ContractId : {}\n \
                   PropertyId : {}\n \
                   PropertyName : {}\n \
                   LatestVersion : {}\n \
                   StagingVersion : {}\n \
                   ProductionVersion : {}\n \
                   AssetId : {}\n ".format(property['accountId'], \
                                           property['propertyId'], \
                                           property['propertyName'], \
                                           property['latestVersion'], \
                                           property['stagingVersion'], \
                                           property['productionVersion'], \
                                           property['contractId'], \
                                           property['propertyId'], \
                                           property['propertyName'], \
                                           property['latestVersion'], \
                                           property['stagingVersion'], \
                                           property['productionVersion'], \
                                           property['assetId'])
            )

    def get_all(self,connection,baseurl,json=True):
        """ get all properties """
        response=connection.get(urljoin(baseurl, self.__papiurl),headers=self.__headers)
        if response.status_code != 200:
           print ('Error {}'.format(response.status_code))
        else:
            if json:
                """get all properties in json format"""
                return response.json()
            else:
                self.reader(response)


    def get_property(self,connection,baseurl,propertyId,json=True):
        """get data for one propiety in json format"""
        papiurl = '/papi/v1/properties/{}?groupId={}&contractId={}'.format(propertyId,self.__groupId,self.__contractId)
        response = connection.get(urljoin(baseurl, papiurl),headers=self.__headers)
        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
        else:
            if json:
                return response.json()
            else:
                self.reader(response)
