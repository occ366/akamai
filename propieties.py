from urllib.parse import urljoin

class propieties:

    __init__(self,groupId,contractId):
        self.__groupId = groupId
        self.__contractId=contractId
        self.__papiurl="/papi/v1/properties?groupId={}&contractId={}".format(groupId,contractId)
  
  
    def getAll(sesson,baseurl,json=true):
  
        response=sesson.get(urljoin(baseurl, self.__papiurl))
        
        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
       
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
              
      def getOnePropiety(sesson,baseurl,propietyId,json=true):
          
          """get data for one propiety in json format"""
          papiurl = '/papi/v1/properties/{}?groupId={}&contractId={}'.format(propietyId,self.__groupId,self.__contractId)
          
          response = sesson.get(urljoin(baseurl, papiurl))
      
             
          if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
          
        else:
            if json: 
                """get all propieties in json format"""
                return response.json()
          
            else:
       
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

      
      
  
