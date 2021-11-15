#!/usr/bin/env python3

from urllib.parse import urljoin

class propieties:

    def __init__(self,groupId,contractId):
        self.__groupId = groupId
        self.__contractId=contractId
        self.__papiurl="/papi/v1/properties?groupId={}&contractId={}".format(groupId,contractId)
        self.__headers = { 'PAPI-Use-Prefixes' : 'true' }
        
    def reader(self,connection):
      """get all propieties in readly format"""
               for propiety in response.json()['properties']['items']:
                   print("---------------------------\n \
                          AccountId {}\n ContractId : {}\n \
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
                          AssetId : {}\n ".format((propiety['accountId'], \
                                                   propiety['propertyId'], \
                                                   propiety['propertyName'], \
                                                   propiety['latestVersion'], \
                                                   propiety['stagingVersion'], \
                                                   propiety['productionVersion'], \
                                                   propiety['assetId']
                                                  )
                                                
                         )
      
      
      
    def getAll(self,connection,baseurl,json=True):
  
        response=connection.get(urljoin(baseurl, self.__papiurl),headers=self.__headers)
        
        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
                reader(response)   
            
              
      def getPropiety(self, connection,baseurl,propietyId,json=True):
          
          """get data for one propiety in json format"""
          papiurl = '/papi/v1/properties/{}?groupId={}&contractId={}'.format(propietyId,self.__groupId,self.__contractId)
          
          response = connection.get(urljoin(baseurl, papiurl),headers=self.__headers)
      
             
          if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
                reader(response) 
