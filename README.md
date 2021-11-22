# akamai

Set of modules to connect to papi akamai apis for managment

__python3 is needed

- cpcode.py  all the methods to get an create cpcodes

- group.py  all the methods to get groups

- hostnames.py  all the methods to get and create edgehostnames over a propiety

- products.py   all the methods to get and creat

- propieties.py  all the methods to get data about propieties

- rules.py  all the methods to get and create rules over porpieties

- main.py main scrip

## modules dependencies

__Must be installed in your system

- requests
- re
- json
- logging
- edgegrid-python [edgegrid-python](https://github.com/akamai/AkamaiOPEN-edgegrid-python)

## Inputs

- File with all the channels, format unix; bucketId, bucket_description(name), hosts
- User credential in file .edgerc

## Outputs

Main create a log file on /tmp/akamai_papi.log by default

