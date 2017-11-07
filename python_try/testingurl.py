import urllib.request
import urllib.parse


#req = urllib.request.urlopen('https://www.google.co.in')
#print(req.read())



values = {'q':'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.co.in/search?'+data
#print(data)
#data = data.encode('utf-8')
 

#oops
#self, *args, **kwargs

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()
print(resp_data)
 
