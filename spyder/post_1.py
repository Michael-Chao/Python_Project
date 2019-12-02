import urllib.parse
import urllib.request
import socket
import urllib.error

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', timeout=1)
print(response.read())