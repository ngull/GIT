#python
import requests
import json
from pprint import pprint

############################################### Logging on APIC ##################################################
### Disable certificate warnings ###
requests.packages.urllib3.disable_warnings()
### Building body data for API resquest ###
encoded_body = json.dumps({
"aaaUser": {
"attributes": {
"name": "admin",
"pwd": "ciscopsdt"
}
}
})
### Making the quest ###
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)
### Storing the received APIC-cookie from the login as a value to be used in subsequent REST calls ####
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}
############################################################################################################

### Making other REST API calls ###
### Making call towards tenant class on the ACI
contracts = requests.get("https://sandboxapicdc.cisco.com/api/node/class/vzBrCP.json", headers=header, verify=False)

### Loading tenants.text into JSON object
json_contracts_dic = json.loads(contracts.text)

### Making the dictionary a list
json_contracts_list = json_contracts_dic['imdata']

### Printing Contracts and DN
print('')
print('')
print('***********************************************')
print('*************** CONTRACTS *********************')
print('****************** DN *************************')
print('')
for cont in json_contracts_list:
    contrato = cont['vzBrCP']['attributes']['name']
    print('Contract name: ', contrato)
    dn = cont['vzBrCP']['attributes']['dn']
    print('Path: ', dn)
    print('')


### Making other REST API calls ###
### Making call towards tenant class on the ACI
EPG_Prov_contracts = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvRsProv.json", headers=header, verify=False)

### Loading tenants.text into JSON object
json_EPG_Prov_contracts_dic = json.loads(EPG_Prov_contracts.text)

### Making the dictionary a list
json_EPG_Prov_contracts_list = json_EPG_Prov_contracts_dic['imdata']

### Printing Contracts EPG and DN
print('')
print('')
print('***********************************************')
print('******** EPG PROVIER CONTRACTS ****************')
print('****************** DN *************************')
print('')
for EPG_Prov in json_EPG_Prov_contracts_list:
    contrato = EPG_Prov['fvRsProv']['attributes']['tnVzBrCPName']
    print('Contract name: ', contrato)
    dn = EPG_Prov['fvRsProv']['attributes']['dn']
    print('EPG: ', dn)
    print('')


### Making other REST API calls ###
### Making call towards tenant class on the ACI
EPG_Cons_contracts = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvRsCons.json", headers=header, verify=False)

### Loading tenants.text into JSON object
json_EPG_Cons_contracts_dic = json.loads(EPG_Cons_contracts.text)

### Making the dictionary a list
json_EPG_Cons_contracts_list = json_EPG_Cons_contracts_dic['imdata']

### Printing Contracts EPG and DN
print('')
print('')
print('***********************************************')
print('******** EPG CONSUMER CONTRACTS ***************')
print('****************** DN *************************')
print('')
for EPG_Cons in json_EPG_Cons_contracts_list:
    contrato = EPG_Cons['fvRsCons']['attributes']['tnVzBrCPName']
    print('Contract name: ', contrato)
    dn = EPG_Cons['fvRsCons']['attributes']['dn']
    print('EPG: ', dn)
    print('')
