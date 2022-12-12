
from urllib import request
url='http://www.google.com'
site=request.urlopen(url)

page=site.read()
print(page)
print('-'*50)
print(site.status)
headers=site.getheaders()
print(headers)

for header in headers:
    print(header[0],'>>',header[1])
