#!/usr/bin/env python3

from urllib.parse import urljoin  

                                                       
class rules:
    
    __init__(self,propietyId,versionId,groupId,contractId):
       
       self.__groupId = groupId
       self.__contractId = contractId
       self.__versionId=versionId
       self.__papiurl="/papi/v1/properties/{}/versions/{}/hostnames?groupId={}&contractId={}".format(propietyId,versionId,groupId,contractId)
    
    
    def getAll(sesson,baseurl,json=True):
  
        response=sesson.get(urljoin(baseurl, self.__papiurl))
        
        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
       
                """get all propieties in readly format"""
                reader(response)
                                                
                          )
    def createSetRules(sesson,baseurl,sent_data):
        """create a set of new rules """
                                
        headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
        result = sesson.put(urljoin(baseurl, self.__papiurl),data=sent_data,headers=headers)
        
        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
          
        else:
            return response.json()

