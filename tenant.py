import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

cookie = {"APIC-cookie": "MT7qJ/E1dSqdMsudUlQPREDP1Aj5yrZVpxO1y+5rpcXaL5btNxxKlS8egtBrr3ecH5ImlYSQKiN97bfYlEVGpp6eEvwvf72litBuKqm38kQnft/YlDiuhqVm1mVMpfeVwKf9+phvamYPu7Rz0vYghFe0JpY95lHtWO9jDqgITxY=" }

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)