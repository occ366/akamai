#!/usr/bin/env python3

from urllib.parse import urljoin  

                                                       
class hostnames:
    
    __init__(self,groupId,contractId):
       
       self.__groupId = groupId
       self.__contractId = contractId
       self.__papiurl="/papi/v1/edgehostnames?{}&{}".format(groupId,contractId)
    
    def reader(JsonToRead):
        
        """get all propieties in readly format"""
                for edgehostname in response.json()['edgehostnames']['items']:
                    print("---------------------------\n \
                           edgeHostnameId {}\n \
                           edgeHostnameDomain : {}\n \
                           productId : {}\n \
                           domainPrefix : {}\n \
                           domainSuffix : {}\n \
                           status : {}\n \
                           secure :  {}\n \
                           ipVersionBehavior : {}".format((edgehostname['edgeHostnameId'], \
                                                           edgehostname['edgeHostnameDomain'], \
                                                           edgehostname['productId'], \
                                                           edgehostname['domainPrefix'], \
                                                           edgehostname['domainSuffix'], \
                                                           edgehostname['status'], \
                                                           edgehostname['secure'], \
                                                           edgehostname['ipVersionBehavior'], \
                                                          )
                                                
                          )
    
    
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
    def createHostname(sesson,baseurl,productId,domain):
        """get data for one propiety in json format"""
        papiurl = "/papi/v1/edgehostnames?groupId={}&contractId={}".format(self.__groupId,self.__contractId)
        
        send_data = """
                       { 
                           "productId": "%s",
                           "domainPrefix": "%s",
                           "domainSuffix": "edgesuite.net",
                           "secureNetwork": "STANDARD_TLS",
                           "ipVersionBehavior": "IPV4"
                        }""" % (productId,domain)
                        
        headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
        result = sesson.post(urljoin(baseurl, self.__papiurl),data=sent_data,headers=headers)
        
        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
          
        else:
            return response.json()
