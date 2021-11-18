#!/usr/bin/env python3

from urllib.parse import urljoin
import json

LOG_PATH='/tmp/akamai_papi.log'
LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)
logger_file_handler = FileHandler(LOG_PATH)
logger_file_handler.setLevel(logging.DEBUG)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler)


class rules:

    def __init__(self,propietyId,versionId,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__versionId=versionId
        self.__papiurl="/papi/v1/properties/{}/versions/{}/rules?groupId={}&contractId={}".format(propietyId,versionId,groupId,contractId)
        self.__oldOriginAndCpcode={}
        self.__newOriginAndCpcode_list=[]
        self.__oldSetRules={}


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
            except e:
               logger.error('Problem to find rules on rules.get()')


    def createSetRules(self,connection,baseurl):
        """create a set of new rules """

        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }

        result = connection.put(urljoin(baseurl, self.__papiurl),data=self.createNewSetOfRules(),headers=headers)

        if response.status_code != 201:
            logger.error ('Error, code {} on rule.createSetRules() call'.format(response.status_code))
            logger.error(response.json())

        else:
            return response.json()


    def addOriginAndCpcode(self,bucketId,name,hostname,cpcodeID):
        """add a new origin and cpcode on Origin & cpcodes """
        if name in self.__oldOriginAndCpcode["children"]:
            logger.info ('rules.addOriginAndCpcode(): Channel {} already Exist'format(name))

        else:
            self.__newOriginAndCpcode_list.append(self.createJson(bucketId,name,hostname,cpcodeID))
            logger.info('rules.addOriginAndCpcode(): Add a new origin&cpcode')


    def createJson(self,bucketId,name,hostname,cpcodeID):
        """ Create json for each new entry """
        edomain="e{}.1.cdn.telefonica.com".format(bucketId)
        send_data = """
                       {
                          "name" : "%s",
                          "children" : [ ],
                          "behaviors" : [ {
                                            "name" : "cpCode",
                                            "options" : {
                                                          "value" : {
                                                                       "id": %s,
                                                                       "description" : "%s",
                                                                       "products" : [ "Adaptive_Media_Delivery" ],
                                                                       "name" : "%s"
                                                                    }
                                                        }
                                           }, {
                                                 "name" : "origin",
                                                 "options" : {
                                                               "originType" : "CUSTOMER",
                                                               "hostname" : "%s",
                                                               "forwardHostHeader" : "ORIGIN_HOSTNAME",
                                                               "cacheKeyHostname" : "ORIGIN_HOSTNAME",
                                                               "compress" : true,
                                                               "enableTrueClientIp" : true,
                                                               "originCertificate" : "",
                                                               "verificationMode" : "CUSTOM",
                                                               "ports" : "",
                                                               "httpPort" : 8000,
                                                               "httpsPort" : 8000,
                                                               "trueClientIpHeader" : "True-Client-IP",
                                                               "trueClientIpClientSetting" : false,
                                                               "originSni" : true,
                                                               "customValidCnValues" : [ "{{Origin Hostname}}", "{{Forward Host Header}}" ],
                                                               "originCertsToHonor" : "STANDARD_CERTIFICATE_AUTHORITIES",
                                                               "standardCertificateAuthorities" : [ "akamai-permissive" ]
                                                              }
                                           }, {
                                                "name" : "originCharacteristics",
                                                "options" : {
                                                "country" : "EUROPE",
                                                "authenticationMethodTitle" : "",
                                                "authenticationMethod" : "AUTOMATIC"
                                              }
                                           } ],
                          "criteria" : [ {
                                           "name" : "hostname",
                                           "options" : {
                                                          "matchOperator" : "IS_ONE_OF",
                                                          "values" : [ "%s" ]
                                                       }
                                         } ],
                         "criteriaMustSatisfy" : "all"
                       }""" % (cpcodeId,name,name,edomain,hostname)

        logger.info('rules.createNewSetOfRules(): New cpcode and origin has been created: ' + send_data)

        return json.dumps(send_data)


    def createNewSetOfRules():
        """build a new json to put in akamai """
        newSetRules = self.__oldSetRules
        newOriginAndCpcode = self.__oldOriginAndCpcode

        newOriginAndCpcode["children"] = self.__newOriginAndCpcode_list
        position = newSetRules["rules"]["children"].index(self.__oldOriginAndCpcode)
        new_rules_children = newSetRules["rules"]["children"].pop(position)
        new_rules_children = new_rule_childre.insert(position,  newOriginAndCpcode)

        newSetRules["rules"]["children"]=new_rules_children

        logger.info('rules.createNewSetOfRules(): New set of rules has been created: ' + newSetRules)

        return newSetRules
