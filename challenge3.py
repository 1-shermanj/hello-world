import requests
##ASA config gotten from examples on ASA sandbox then python code fro postman
url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers)

print(response.text)

## for nx config use firefox to go to sandbox b/c it can do pop up for python code as patch not post command
## enter in your code select python and copy then paste here and modify fields

import requests
import json

"""
Modify these please
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vlan 600 ; name Construction ;vlan 700 ; name Analysis",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


##ios XE config http://192.168.10.80/restconf/api/config/native/ip/route?deep in postman  chode patch instead of put
## copy the config and paste it in a post body, modify then select code for python ans paste here


import requests

url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{\n    \"ned:route\": {\n        \"ip-route-interface-forwarding-list\": [\n            {\n                \"prefix\": \"216.48.1.0\",\n                \"mask\": \"255.255.255.0\",\n                \"fwd-list\": [\n                    {\n                        \"fwd\": \"10.1.1.1\"\n                    }\n                ]\n            }\n        ],\n        \"static\": {}\n    }\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)


#########################
#trying a new static route
import requests

url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{\n    \"ned:route\": {\n        \"ip-route-interface-forwarding-list\": [\n            {\n                \"prefix\": \"5.5.5.5\",\n                \"mask\": \"255.255.255.255\",\n                \"fwd-list\": [\n                    {\n                        \"fwd\": \"200.0.0.0\"\n                    }\n                ]\n            }\n        ],\n        \"static\": {}\n    }\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
