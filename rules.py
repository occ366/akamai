#!/usr/bin/env python3

import json
import re

import logging
logger = logging.getLogger(__name__)


class rules:

    def __init__(self,propietyId,versionId,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__versionId=versionId
        self.__papiurl="/papi/v1/properties/{}/versions/{}/rules?groupId={}&contractId={}".format(propietyId,versionId,groupId,contractId)
        self.__oldOriginAndCpcode={}
        self.__newOriginAndCpcode_list=[]
        self.__oldSetRules={}


    def getAll(self,connection):

        response=connection.get(self.__papiurl))
        self.__oldSetRules=response.json()

        try:
            for children in response.json()["rules"]["children"]:
                if children["name"] in 'Origins & CP Codes':
                   self.__newOriginAndCpcode_list = children["children"]
                   self.__oldOriginAndCpcode = children
        except:
           logger.error('Problem to find rules on rules.get()')


    def createSetRules(self,connection):

        """create a set of new rules """

        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }
        result = connection.put(self.__papiurl,data=self.createNewSetOfRules(),headers=headers)

        logger.info('rules.createSetRules(): Create a new set of rules')
        logger.info( response.json())


    def addOriginAndCpcode(self,bucketId,name,hostname,cpcodeID)

        """add a new origin and cpcode on Origin & cpcodes, if not exist """
        NotExist = True
        for originAndCpcode in self.__oldOriginAndCpcode["children"]:

            if name in originAndCpcode["name"]:
                NotExist =  False


        if NotExist:
            self.__newOriginAndCpcode_list.append(self.createJson(bucketId,name,hostname,cpcodeID))
            logger.info('rules.addOriginAndCpcode():  origin and cpcode for channel {} created'.format(name))

        else:
            logger.info('rules.addOriginAndCpcode(): Channel {} already Exist'.format(name))



    def createJson(self,bucketId,name,hostname,cpcodeId):

        """ Create json for each new entry """
        edomain="e{}.1.cdn.telefonica.com".format(bucketId)

        cpCodeId=int(re.sub('cpc_','',cpcodeId))

        #TO DO, extract a jsmodel forn origins and cpcodes, an just remolace values by keys
        send_data = { "name" : name, "children": [ ],"behaviors" : [ {"name" : "cpCode","options" : { "value" : \
                    { "id": cpCodeId,"description" : name ,"products" : [ "Adaptive_Media_Delivery" ],"name" : name}}}, {"name" : "origin", \
                      "options" : {"originType" : "CUSTOMER","hostname" : edomain,"forwardHostHeader" : "ORIGIN_HOSTNAME", \
                      "cacheKeyHostname" : "ORIGIN_HOSTNAME","compress" : True ,"enableTrueClientIp" : True ,"originCertificate" : "",\
                      "verificationMode" : "CUSTOM","ports" : "","httpPort" : 8000,"httpsPort" : 8000,"trueClientIpHeader" : "True-Client-IP",\
                      "trueClientIpClientSetting" : False ,"originSni" : True ,"customValidCnValues" : [ "{{Origin Hostname}}", "{{Forward Host Header}}" ], \
                      "originCertsToHonor" : "STANDARD_CERTIFICATE_AUTHORITIES","standardCertificateAuthorities" : [ "akamai-permissive" ]} \
                    }, {"name" : "originCharacteristics","options" : {"country" : "EUROPE","authenticationMethodTitle" : "", \
                        "authenticationMethod" : "AUTOMATIC"}} ],"criteria" : [ {"name" : "hostname","options" : { "matchOperator" : "IS_ONE_OF", \
                        "values" : [ hostname ]}} ],"criteriaMustSatisfy" : "all"}

        logger.info('rules.createNewSetOfRules(): New cpcode and origin has been created: {}'.format(send_data))

        return send_data


    def createNewSetOfRules(self):

        """build a new json to put in akamai """
        newSetRules = self.__oldSetRules
        newOriginAndCpcode = self.__oldOriginAndCpcode

        newOriginAndCpcode["children"] = self.__newOriginAndCpcode_list

        index=0

        for children in newSetRules["rules"]["children"]:
            if children['name']  in 'Origins & CP Codes':
                newSetRules["rules"]["children"][index]=newOriginAndCpcode
            else:
                index+=1

        newSetRules['warnings']=[]
        newSetRules['errors']=[]

        logger.info('rules.createNewSetOfRules(): New set of rules has been created: {}'.format(newSetRules))

        return json.dumps(newSetRules)



    def getCreatedOriginAndCpcodes(self):

        print(self.__newOriginAndCpcode_list)

