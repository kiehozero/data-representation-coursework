import requests
import urllib.parse
from config import conkeys as cfg

url = 'https://en.wikipedia.org'

apiKey = cfg['htmltopdf']

api_url = 'https://api.html2pdf.app/v1/generate'

params = {'url': url, 'apiKey': apiKey}
parsedParams = urllib.parse.urlencode(params)
request_url = api_url + '?' + parsedParams

response = requests.get(request_url)

print(response.status_code)

result = response.content

with open('document.pdf', 'wb') as handler:
    handler.write(result)