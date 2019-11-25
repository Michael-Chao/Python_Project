import urllib.request

url = "http://www.baidu.com"
responces = urllib.request.urlopen(url)
html = responces.read()
html = html.decode('utf-8')
print(html)

fileOb = open('html.txt','w',encoding='utf-8')
fileOb.write(html)
fileOb.close()