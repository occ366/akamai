#!/usr/bin/env python3

import requests
import re
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin
from cpcode import cpcode
from hostnames import hostnames
from rules import rules

def main():

    path_file = '/home/ocuellas/buckets_tde_live.txt'
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

    cp = cpcode(groupId,contractId)
    hn = hostnames(groupId,contractId)
    rl = rules(propietyId,versionId,groupId,contractId)

    cpc.getAll(connect,baseurl,True)
    hn.getAll(connect,baseurl,True)
    rl.getAll(connect,baseurl,True)
    newChildrens=[]

    with open(path_file)  as file :

        for line in file.readlines():

            bucketId,name,hostname = line.split()
            hostname=re.sub('[\["\]]','',hostname)

            #create hostname and add to the propiety
            hn.createHostname(connect,baseurl,productId,hostname)
            hn.addHostnameToPropiety(connect,baseurl,propietyId,versionId,hostname)

            #create a cpcode for one bucket
            respose_cpc=cpc.createCPcode(connect,baseurl,productId,name,json=True)
            cpcodeID = re.search(r'cpc_\d+', response_cpc['cpcodeLink'])[0]

            #build the rules for this  step
            newChilderns.append(rl.createJson(bucketId,name,hostname,re.sub('cpc_','',cpcodeID)))

    #update the new rules on the propiety.
    

    #g = group()
    #response = g.get(connect,baseurl)
    #print(response.json())

    #ps = propieties(groupId,contractId)
    #print(ps.getAll(connect,baseurl,False))
    #print(ps.getPropiety(connect,baseurl,propietyId,json=False))

    #cpc = cpcode(groupId,contractId)
    #print(cpc.getAll(connect,baseurl,False))
    #print(cpc.getCPcode(connect,baseurl,'cpc_1185062',False))
    #print(cpc.createCPcode(connect,baseurl,productId,cpcodeName,json=True))

    #hn = hostnames(groupId,contractId)
    #print(hn.getAll(connect,baseurl,False))
    #print(hn.createHostname(connect,baseurl,productId,domain))
    #print(hn.addHostnameToPropiety(connect,baseurl,propietyId,versionId,domain))

    #r = rules(propietyId,versionId,groupId,contractId)
    #print(r.getAll(connect,baseurl,True))

if __name__ == "__main__":
    main()

