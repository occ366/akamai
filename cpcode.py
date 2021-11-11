#!/usr/bin/env python3

from urllib.parse import urljoin 

class cpcodes:
    
    __init__(self,groupId,contractId):
       
       self.__groupId = groupId
       self.__contractId = contractId
       self.__papiurl="/papi/v1/cpcodes?{}&{}".format(groupId,contractId)
       
    def reader(JsonToread):
        """get all propieties in readly format"""
        for cpcode in response.json()['cpcodes']['items']:
             print("---------------------------\n \
                    cpcodeId {}\n \
                    cpcodeName : {}\n \
                    productIds : {}\n \
                    createdDate : {}\n ".format((cpcode['cpcodeId'], \
                                                 cpcode['cpcodeName'], \
                                                 cpcode['productIds'], \
                                                 cpcode['createdDate'], \
                                                )
                                                
                          )
    def getAll(sesson,baseurl,json=True):
        """get all propieties in json format"""
        headers = { 'PAPI-Use-Prefixes' : 'true' }
        response=sesson.get(urljoin(baseurl, self.__papiurl),headers = headers)
        
        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
                reader(response)
       
                
    def getCPcode(sesson,baseurl,cpcodeId):
        """get data for one propiety in json format"""
        papiurl = '/papi/v1/cpcodes/{}?groupId={}&contractI={}'.format(cpcodeId,self.__groupId,self.__contractId)
        headers = { 'PAPI-Use-Prefixes' : 'true' }
         
        response=sesson.get(urljoin(baseurl, papiurl),headers=headers)
        
        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
          
        else:
            
            return response.json()
          
            else:
                reader(response)
                                                
                  
    def createCPcode(sesson,baseurl,productId,cpcodeName,Json=True):
        
        """create a new CPcode"""
                send_data = """
                      { 
                          "productId": "%s",
                          "cpcodeName": "%s"
                      }""" % (productId,cpcodeName)
                      
        headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
        result = sesson.post(urljoin(baseurl, self.__papiurl),data=sent_data,headers=headers)
        
        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
          
        else:
            return response.json()