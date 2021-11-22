#!/usr/bin/env python3

import json
import re

import logging
logger = logging.getLogger(__name__)


class hostnames:

    def __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/edgehostnames?groupId={}&contractId={}".format(groupId,contractId)
        self.__allhostname={}

    def reader(self,response):
        """get all propieties in readly format"""
        try:
            for edgehostname in response.json()['edgeHostnames']['items']:
                print("---------------------------\n \
                       EdgeHostnameId {}\n \
                       EdgeHostnameDomain : {}\n \
                       DomainPrefix : {}\n \
                       DomainSuffix : {}\n \
                       Status : {}\n \
                       Secure :  {}\n \
                       IpVersionBehavior : {}".format(edgehostname['edgeHostnameId'], \
                                                      edgehostname['edgeHostnameDomain'], \
                                                      edgehostname['domainPrefix'], \
                                                      edgehostname['domainSuffix'], \
                                                      edgehostname['status'], \
                                                      edgehostname['secure'], \
                                                      edgehostname['ipVersionBehavior'])
                     )
        except:
            logger.error('hostnames.reader(), Error on values'))


    def getAll(self,connection,json=True):

        response=connection.get(urljoin(baseurl, self.__papiurl))
        self.__allhostnames=response.json()

        if json:
            """get all hostnames in json format"""
            return response.json()

        else:

            """get all hostnames in readly format"""
            self.reader(response)


    def createHostname(self,connection,productId,domain):

        if self.checkIfExist(domian):
            logger.info("hostname.createHostname(): Domain {} exists already!!!".format(domain))

        else:
            """get data for one propiety in json format"""
            papiurl = "/papi/v1/edgehostnames?groupId={}&contractId={}".format(self.__groupId,self.__contractId)

            send_data = """{"productId": "%s","domainPrefix": "%s","domainSuffix": "edgesuite.net","secureNetwork": "STANDARD_TLS","ipVersionBehavior": "IPV4"}""" % (productId,domain)
            headers = { 'PAPI-Use-Prefixes' : 'true' }
            response = connection.post(self.__papiurl),data=send_data,headers=headers)

            logger.info("hostname.createHostname(): Domain {} created".format(domain))
            return response.json()



    def checkIfExist(self,domain):
        """ check if the hostname exist  """
        for edgehostname in self.__allhostname['edgeHostnames']['items']:
            if domain in edgehostname['edgeHostnameDomain']:
                return = True

        return False


    def addHostnameToPropiety(self,connection,baseurl,propietyId,versionId,domain):
        """ add a cerate hostname to a version of one propiety  """

        papiurl = "/papi/v1/properties/{}/versions/{}/hostnames?groupId={}&contractId={}&validateHostnames=true&includeCertStatus=true"\
                         .format(propietyId,versionId,self.__groupId,self.__contractId)

        domainWsub= domain+'.edgesuite.net'

        send_data = """{"add":[{"cnameType": "EDGE_HOSTNAME","cnameFrom": "%s","cnameTo": "%s"}]}""" % (domain,domainWsub)
        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }
        response = connection.patch(papiurl,data=send_data,headers=headers)


        logger.info("hostname.addHostnameToPropiety(): Domain {} add to the propirty {}".format(domain,propietyId))
        return response.json()


    def getHostname(connection,baseurl,edgeHostnameId,contractId,groupId,options):
        """ get data of one edgeHostname """
        pass
        #TO DO
