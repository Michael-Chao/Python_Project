import requests

url = 'http://live.v.news.cn/pc/play_three.html?roomId=2263'

fout = open('result.txt', 'w')

for i in range(1000000000000000):

    r = requests.post(url)

    fout.write(url+' ： OK withstatus_code: '+str(r.status_code))

    print(url+' ： OK withstatus_code: '+str(r.status_code))

fout.close()
