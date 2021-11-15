#!/usr/bin/env python3

import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin
from group import group
from propieties import propieties

def main():

    path_credential='~/.edgerc'
    section = 'default'


    edgerc = EdgeRc(path_credential)
    baseurl = 'https://%s' % edgerc.get(section, 'host')
    connect = requests.Session()
    connect.auth = EdgeGridAuth.from_edgerc(edgerc, section)

    g = group()
    response = g.get(connect,baseurl)
    print(response.json())
    
    ps = propieties('grp_190994','ctr_P-3RG8LCE')
    print(ps.getAll(connect,baseurl,False))
    print(ps.getPropiety(connect,baseurl,'prp_694869',json=False))

if __name__ == "__main__":
    main()
