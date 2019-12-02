from requests import Session
s = Session()
s.get('http://httpbin.org/cookies/set/number/1234567')
r = s.get('http://httpbin.org/cookies')
print(r.text)