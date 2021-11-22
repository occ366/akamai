#!/usr/bin/env python3

import requests
import re
from connection import connection
from cpcode import cpcode
from hostnames import hostnames
from rules import rules

import logging
from logging import FileHandler
from logging import Formatter


LOG_PATH='/tmp/akamai_papi.log'
LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)
logger_file_handler = FileHandler(LOG_PATH)
logger_file_handler.setLevel(logging.DEBUG)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler)

def main():

    path_file = '/home/ocuellas/buckets_tde_live.txt'
    path_credential='~/.edgerc'
    section = 'jorge'
    groupId='grp_93936'
    contractId='ctr_M-20JBZC4'
    propietyId='prp_678848'
    productId = 'prd_Adaptive_Media_Delivery'
    versionId='13'


    connect = connection(path_credential,section)
    cp = cpcode(groupId,contractId)
    hn = hostnames(groupId,contractId)
    rl = rules(propietyId,versionId,groupId,contractId)

    cpc.getAll(connect,True)
    hn.getAll(connect,True)
    rl.getAll(connect)

    try:
        with open(path_file)  as file :

           for line in file.readlines():

               bucketId,name,hostname = line.split()
               hostname=re.sub('[\["\]]','',hostname)

               #create hostname and add to the propiety
               hn.createHostname(connect,baseurl,productId,hostname)
               hn.addHostnameToPropiety(connect,baseurl,propietyId,versionId,hostname)

               #create a cpcode for one bucket
               respose_cpc=cpc.createCPcode(connect,productId,name,json=True)
               cpcodeID = re.search(r'cpc_\d+', response_cpc['cpcodeLink'])[0]

               #build the rules for this  step
               rl.addOriginAndCpcode(bucketId,name,hostname,cpcodeID)


    except:
        print('main(): file '+ str(self.__path_file) + ' doesnt exist')
        logger.error('main(): file '+ str(self.__path_file) + ' doesnt exist')
        exit(1)

    #update the new rules on the propiety.
    rl.createSetRules(connection,baseurl)

    connect.close()


if __name__ == "__main__":
    main()

