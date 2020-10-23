import requests
import sys
import json

### Getting accessToken
url = "https://api.ultradns.com/authorization/token"

payload = 'grant_type=password&username=kevin&password=***********'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.post(url, data = payload)
output = json.loads(response.text)
token = output['accessToken']

### HTTP UltraDNS API request
zone = sys.argv[1]
file = sys.argv[2]
IP = sys.argv[3]

with open(f'{file}', 'r') as a_file:
    mylist = list(a_file)
    subdomain = [a.strip() for a in mylist]
    for i in range(len(subdomain)):
        url = f"https://api.ultradns.com/zones/{zone}/rrsets/A/{subdomain[i]}"
        payload = f"{{\r\n\"ttl\": 300,\r\n\"rdata\": [\r\n\"{IP}\"\r\n]\r\n}}"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        response = requests.put(url, headers = headers, data = payload)
        print(response.text.encode('utf8'))
