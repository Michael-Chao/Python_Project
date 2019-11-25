import urllib.request

response = urllib.request.urlopen('http://yzb.buaa.edu.cn/')
word = response.read()
second = word.decode('utf-8')
print(word)

f = open("spyder3.txt", "w", encoding="utf-8")
f.write(word.decode('utf-8'))#直接response不行
f.close()
