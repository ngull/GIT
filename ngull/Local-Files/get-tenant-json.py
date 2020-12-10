#python
import requests
import json

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
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)
#print(tenants.text)

### Loading tenants.text into JSON object
json_response = json.loads(tenants.text)

### This line prints the elements dumps() method returns from the json_response. The arguments control how the output is displayed. ###
#print(json.dumps(json_response, sort_keys=True, indent=4))


###  loop through the tenants within a dictionary, first get the tenants using the json library.
### Then, use a Python for loop to go through each element of the list.
### A second loop won't be required, as the list contained within the children element returned only contains a single value,healthInst.

json_tenants = json_response['imdata']
for tenant in json_tenants:
 tenant_name = tenant['fvTenant']['attributes']['name']
 tenant_dn = tenant['fvTenant']['attributes']['dn']
 tenant_health = tenant['fvTenant']['children'][0]['healthInst']['attributes']['cur']
 output = "Tenant: " + tenant_name + "\t Health Score: " + tenant_health + "\n DN: " + tenant_dn
 print(output.expandtabs(40))
