 #!/usr/bin/env python3

import requests
import re
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin
from group import group
from propieties import propieties
from cpcode import cpcode
from hostnames import hostnames
from rules import rules

def main():

    path_file = '/home/ocuellas/buckets_tde_live.txt'
    path_credential='~/.edgerc'
    section = 'ocuellas'
    groupId='grp_190994'
    contractId='ctr_P-3RG8LCE'
    propietyId='prp_694869'
    productId = 'prd_Adaptive_Media_Delivery'
    versionId='20'

    edgerc = EdgeRc(path_credential)
    baseurl = 'https://%s' % edgerc.get(section, 'host')
    connect = requests.Session()
    connect.auth = EdgeGridAuth.from_edgerc(edgerc, section)

    cp = cpcode(groupId,contractId)
    hn = hostnames(groupId,contractId)
    rl = rules(propietyId,versionId,groupId,contractId)

    with open(path_file)  as file :

        for line in file.readlines():

            bucketId,name,hostname = line.split()
            hostname=re.sub('[\["\]]','',hostname)

            


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
