#!/usr/bin/env python3

import requests
import re
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin
from cpcode import cpcode
from hostnames import hostnames
from rules import rules

import logging

global logger

LOG_PATH='/tmp/akamai_papi.log'
LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.FileHandler(LOG_PATH)
logger_file_handler.setLevel(logging.DEBUG)
logger_file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler)



def main():

    path_file = '/home/ocuellas/prueba_telemadrid.txt'
    path_credential='~/.edgerc'
    section = 'jorge'
    groupId='grp_93936'
    contractId='ctr_M-20JBZC4'
    propietyId='prp_678848'
    productId = 'prd_Adaptive_Media_Delivery'
    versionId='13'

    edgerc = EdgeRc(path_credential)
    baseurl = 'https://%s' % edgerc.get(section, 'host')
    connect = requests.Session()
    connect.auth = EdgeGridAuth.from_edgerc(edgerc, section)

    logger.info('------- Starting a new Execution---------')

    try:

        cpc = cpcode(groupId,contractId)
        hn = hostnames(groupId,contractId)
        rl = rules(propietyId,versionId,groupId,contractId)

    except:

        logger.error('Error on create objets: cpcode, hostname or rules')

    logger.info('Getting al the Json and info needed from Akamai')

    cpc.getAll(connect,baseurl,True)
    hn.getAll(connect,baseurl,True)
    rl.getAll(connect,baseurl)

    try:
        with open(path_file)  as file :

             for line in file.readlines():

                 bucketId,name,hostname = line.split()
                 hostname=re.sub('[\["\]]','',hostname)

                 logger.info('updating bucket: {}'.format(bucketId))


                 #create hostname and add to the propiety
                 hn.createHostname(connect,baseurl,productId,hostname)
                 hn.addHostnameToPropiety(connect,baseurl,propietyId,versionId,hostname)

                 #create a cpcode for one bucket
                 cpcodeID = cpc.createCPcode(connect,baseurl,productId,name)

                 #build the rules for this  step
                 rl.addOriginAndCpcode(bucketId,name,hostname,cpcodeID)



    except:
        logger.error('main(): file {} doesnt exist'.format(path_file))
        exit(1)

    #update the new rules on the propiety.
    rl.createSetRules(connect,baseurl)

    logger.info('----- End execution ------')

    connect.close()


if __name__ == "__main__":
    main()

