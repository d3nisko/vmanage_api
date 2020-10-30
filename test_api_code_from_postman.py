import requests
from pprint import pprint
import json

url = "https://10.10.20.90:8443/dataservice/statistics/interface"

payload = {}
headers = {
  'X-XSRF-TOKEN': '1C295AE2625C90C285E0E1A577010E73CD747AF9E4B60C88083678830D874C918A1FC73176E2D0C392ADEB0C74A4B5D8D456',
  'Cookie': 'JSESSIONID=9RqYQJJ6Xk92lJb1hGq0BYSJ2NVCRYXclYl_Uq2w.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("GET", url, headers=headers, verify=False, data = payload)

print(response.text.encode('utf8'))
