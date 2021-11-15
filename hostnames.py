#!/usr/bin/env python3

from urllib.parse import urljoin


class hostnames:

    def __init__(self,groupId,contractId):

        self.__groupId = groupId
        self.__contractId = contractId
        self.__papiurl="/papi/v1/edgehostnames?groupId={}&contractId={}".format(groupId,contractId)

    def reader(self,response):
        """get all propieties in readly format"""
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


    def getAll(self,connection,baseurl,json=True):

        response=connection.get(urljoin(baseurl, self.__papiurl))

        if response.status_code != 200:
            print ('Error {}'.format(response.status_code))
            print (response.json())

        else:
            if json:
                """get all hostnames in json format"""
                return response.json()

            else:

                """get all hostnames in readly format"""
                self.reader(response)


    def createHostname(self,connection,baseurl,productId,domain):
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
        response = connection.post(urljoin(baseurl, self.__papiurl),data=send_data,headers=headers)

        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
            print(response.json())

        else:
            return response.json()


    def addHostnameToPropiety(propietyId,versionId,domain):
        papiurl = "/papi/v1/properties/{}/versions/{}/hostnames?groupId={}&contractId=\
                               {}&validateHostnames=true&includeCertStatus=true".format(propietyId,versionId,self.__groupId,self.__contractId)
        send_data = """
                       {
                           "add": [
                                    {
                                       "cnameType": "EDGE_HOSTNAME",
                                       "cnameFrom": "%s",
                                       "cnameTo": "%s.edgesuite.net"
                                     }
                                  ]
                        }""" % (domain,domain)

        headers = { 'Content-Type' : 'application/json' , 'PAPI-Use-Prefixes' : 'true' }
        response = connection.post(urljoin(baseurl, self.__papiurl),data=send_data,headers=headers)

        if response.status_code != 201:
            print ('Error {}'.format(response.status_code))
            print (response.json())

        else:
            return response.json()

