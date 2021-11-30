#!/usr/bin/env python3

from urllib.parse import urljoin
import json

import logging
from logging import FileHandler
from logging import Formatter

import logging
logger = logging.getLogger(__name__)

class Hostnames:

    def __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/edgehostnames?groupId={}&contractId={}".format(groupId,contractId)


    def reader(self,response):
        """get all propieties in readly format"""
        try:
            for edgehostname in response.json()['edgehostnames']['items']:
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
            logger.error('hostnames.reader(), Error on values')


    def get_all(self,connection,baseurl,json=True):

        response=connection.get(urljoin(baseurl, self.__papiurl))

        if response.status_code != 200:
            logger.error ('cpcode.getall(): Error, code {} on call'.format(response.status_code))
            logger.error (response.json())

        else:
            self.__allhostnames=response.json()
            if json:
                """get all hostnames in json format"""
                return response.json()

            else:

                """get all hostnames in readly format"""
                self.reader(response)


    def create_hostname(self,connection,baseurl,productId,domain):

        if self.check_if_exist(domain):
            logger.info("hostname.create_hostname(): Domain {} exists already!!!".format(domain))

        else:
            
            papiurl = "/papi/v1/edgehostnames?groupId={}&contractId={}".format(self.__groupId,self.__contractId)

            send_data = """
                           {
                              "productId": "%s",
                              "domainPrefix": "%s",
                              "domainSuffix": "edgesuite.net",
                              "secureNetwork": "STANDARD_TLS",
                              "ipVersionBehavior": "IPV4"
                           }""" % (productId,domain)

            headers = {'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' ,'PAPI-Use-Prefixes' : 'true' }
            response = connection.post(urljoin(baseurl, self.__papiurl),data=send_data,headers=headers)

            if response.status_code != 201:
                logger.error ('hostname.create_hostname(): Error, code {} on call'.format(response.status_code))
                logger.error (response.json())

            else:
                logger.info ('hostname.create_hostname(): Hostname create: {}'.format(domain))



    def check_if_exist(self,domain):

        """ check if the hostname exist  """

        for edgehostname in self.__allhostnames['edgeHostnames']['items']:
            if domain in edgehostname['edgeHostnameDomain']:
                return  True

        return False


    def add_hostname_to_propiety(self,connection,baseurl,propietyId,versionId,domain):
        
        """ add a create hostname to a version of one propiety  """

        papiurl = "/papi/v1/properties/{}/versions/{}/hostnames?groupId={}&contractId={}&validateHostnames=true&includeCertStatus=true"\
                         .format(propietyId,versionId,self.__groupId,self.__contractId)

        domainWsub= domain+'.edgesuite.net'

        send_data = """{"add":[{"cnameType": "EDGE_HOSTNAME","cnameFrom": "%s","cnameTo": "%s"}]}""" % (domain,domainWsub)
        headers = { 'Accept':'*/*' , 'Accept-Encoding':'gzip, deflate, br' , 'Content-Type':'application/json' , 'PAPI-Use-Prefixes':'true' }
        response = connection.patch(urljoin(baseurl, papiurl),data=send_data,headers=headers)

        if response.status_code != 200:
            logger.error ('hostname.addHostnameToPropiety(): Error, code {} on call'.format(response.status_code))
            logger.error (response.json())

        else:
            logger.info('hostname.addHostnameToPropiety(): hostname added: {}'.format(domain))


    def get_hostname(connection,baseurl,edgeHostnameId,contractId,groupId,options):
        """ get data of one edgeHostname """
        pass
        #TO DO
