#!/usr/bin/env python
# coding=utf8

import httplib

httpClient = None





#http://flight.qunar.com/twell/flight/inter/search?depCity=%E4%B8%8A%E6%B5%B7&arrCity=%E9%A6%99%E6%B8%AF&depDate=2017-03-30&adultNum=1&childNum=0&from=flight_int_search&ex_track=&es=MP1VS3tuZxT%2BZ%2B9uJ5TVStaiJ5vavD9OJ5BM%3D%3D%3D%3D%7C1479811022546&retDate=2017-04-19
try:
    httpClient = httplib.HTTPConnection('bj.lianjia.com','80', timeout=300)
    httpClient.request('GET', 'api/newhouserecommend?type=1&query=http%3A%2F%2Fbj.lianjia.com%2Fershoufang%2Frs%25E9%25A1%25BA%25E4%25B9%2589%25E4%25B8%25AD%25E6%2599%259F%25E5%25B9%25BF%25E5%259C%25BA%2F')

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()



