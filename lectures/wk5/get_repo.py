import json
import requests

filename = 'repos-public.json'

url = 'https://api.github.com/repos/kiehozero/data-representation-coursework/contents'

response = requests.get(url)

print(response.status_code)

repo_json = response.json()

with open(filename, 'w') as fp:
    json.dump(repo_json, fp, indent=4)