#!/usr/bin/env python3

from urllib.parse import urljoin
import json
import re

import logging
logger = logging.getLogger(__name__)

class rules:

    def __init__(self,propietyId,versionId,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__versionId=versionId
        self.__propietyId = propietyId

        self.__papiurl="/papi/v1/properties/{}/versions/{}/rules?groupId={}&contractId={}".format(propietyId,versionId,groupId,contractId)

    def getAll(self,connection,baseurl):

        response=connection.get(urljoin(baseurl, self.__papiurl))

        if response.status_code != 200:
            logger.error('rules.getAll(): Error, code {} on rules.getall() call'.format(response.status_code))
            logger.error(response.json())

        else:
            self.__oldSetRules=response.json()
            try:
                for children in response.json()["rules"]["children"]:
                    if children["name"] in 'Origins & CP Codes':
                       self.__newOriginAndCpcode_list = children["children"]
                       self.__oldOriginAndCpcode = children

            except:
               logger.error('rule.getall(): Problem to find rules')


    def createSetRules(self,connection,baseurl):

        """create a set of new rules """

        papiurl='/papi/v1/properties/{}/versions/{}/rules?groupId={}&contractId={}&validateRules=false'.format(self.__propietyId,self.__versionId,self.__groupId,self.__contractId)

        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }

        send_data = self.createNewSetOfRules()

        response = connection.put(urljoin(baseurl, papiurl),data=send_data,headers=headers)

        if response.status_code != 201:
            logger.error('rules.createSetRules(): Error, code {} on call'.format(response.status_code))
            logger.error(response.json())

        else:
            logger.info('rules.createSetRules(): Create a new set of rules')
            logger.info(response.json())


    def addOriginAndCpcode(self,bucketId,name,hostname,cpcodeID):

        """add a new origin and cpcode on Origin & cpcodes """

        if name in self.__oldOriginAndCpcode["children"]:
            logger.info('rules.addOriginAndCpcode(): Channel {} already Exist'.format(name))

        else:
            self.__newOriginAndCpcode_list.append(self.createJson(bucketId,name,hostname,cpcodeID))
            logger.info('rules.addOriginAndCpcode(): Add a new origin&cpcode')


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
        #position = self.__oldSetRules["rules"]["children"].index(self.__oldOriginAndCpcode)

        #new_rules_children = newSetRules["rules"]["children"].pop(position)
        #new_rules_children = new_rule_childre.insert(position,  newOriginAndCpcode)

        #newSetRules["rules"]["children"]=new_rules_children

        logger.info('rules.createNewSetOfRules(): New set of rules has been created: {}'.format(newSetRules))

        return json.dumps(newSetRules)



    def getCreatedOriginAndCpcodes(self):

        print(self.__newOriginAndCpcode_list)
