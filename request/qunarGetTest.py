#!/usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import gzip, cStringIO
import json
import sys


#航班列表页（国际）
type = sys.getfilesystemencoding()
response = None


print "------------------------------"
print "----------国际往返------------"

getDepCity = raw_input('起飞城市：')
getArrCity = raw_input('到达城市：')
getArrTime = raw_input('起飞时间（yyyy-MM-dd）：')
getReturnTime = raw_input('返回时间（yyyy-MM-dd）：')

data = urllib.urlencode({
    'depCity': getDepCity,
    'arrCity': getArrCity,
    'depDate': getArrTime,
    'adultNum': 1,
    'childNum': 0,
    'from': 'flight_int_search',
    'ex_track': '',
    'es': 'MP1VS3tuZxT%2BZ%2B9uJ5TVStaiJ5vavD9OJ5BM%3D%3D%3D%3D%7C1479811022546',
    'retDate': getReturnTime
})

url = 'http://flight.qunar.com/twell/flight/inter/search?%s' % data

#print url

#http://flight.qunar.com/twell/flight/inter/search?depCity=%E4%B8%8A%E6%B5%B7&arrCity=%E9%A6%99%E6%B8%AF&depDate=2017-03-30&adultNum=1&childNum=0&from=flight_int_search&ex_track=&es=MP1VS3tuZxT%2BZ%2B9uJ5TVStaiJ5vavD9OJ5BM%3D%3D%3D%3D%7C1479811022546&retDate=2017-04-19

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control' : 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'QN99=1673; QN1=eIQjmVjSMNieLE4uEft6Ag==; QN205=organic; QunarGlobal=10.86.213.123_483c1464_15af50ace27_-5191|1490170072547; QN269=A5ED6C000ED611E79386FA163E620FF6; QN601=88bcfc74541d5143b3233b1343f43e6b; QN170=106.38.61.184_aee05d_0_%2B1Hs%2BVcD6DQUFENySjW2RwDiReBqtvwUerU8Tep3psc%3D; SplitEnv=D; csrfToken=KnazClddEvUyv7fB1lffBPasJIfJAtnE; flight.trends=%u5317%u4EAC-%u4E0A%u6D77%3B%u5317%u4EAC-%u5E7F%u5DDE; nts_trace=9d17f8624fc0A; RT=s=1490771639054&r=http%3A%2F%2Fflight.qunar.com%2F; _i=RBTKSomu1gRxzUCxst47MKzxnMmx; _vi=VPyD_y4cy2xm6mI59N3T2Ajkc9fVaJG3m4SizzDJX087HorjZvV9V6UsFT5I6Lzb5KJ-zUuQsF1MvtHZ_Qve9B4En-mOZ-JtrCYilw0zxARl7DBwqH51F8xEpr12ebx_o-OSb9LWa8RH5qWYhzPHPti6yjkv5Dy8AZoGcN2mjHnB; QN621=1490067914133%3DA%26fr%3Dflight_int_search',
        'Host': 'flight.qunar.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

try:
    req = urllib2.Request(url, headers=header)
    response=urllib2.urlopen(req)
    #print response.headers['Content-Type']

    resJson = response.read()
    if resJson[:6] == '\x1f\x8b\x08\x00\x00\x00':
        resJson = gzip.GzipFile(fileobj=cStringIO.StringIO(resJson)).read()

    parsed_json = json.loads(json)
    gettotalPrices = parsed_json['result']['most'][0]['totalPrice']
    getArr = parsed_json['result']['ctrlInfo']['arr']['cityZh'].encode('UTF-8')
    getDep = parsed_json['result']['ctrlInfo']['dep']['cityZh'].encode('UTF-8')

    print "------------------------------"
    print "起飞城市：" + str(getDep)
    print "到达城市：" + str(getArr)
    print "起飞时间：" + getArrTime
    #print "最低价：" + str(getlowPrices)
    print "最低价：" + str(gettotalPrices)
    print "------------------------------"

except Exception, e:
    print 'Invalid input', e
    print '搜索无结果，请校验输入格式'



finally:
    if response:
        response.close()

