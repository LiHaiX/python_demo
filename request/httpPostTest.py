#!/usr/bin/env python
# coding=utf8

import httplib, urllib
import sys
sys.getfilesystemencoding()

httpClient = None
try:
    params = urllib.urlencode(
        {"businessId":23690,
         "persons":[{"personId":1000000020329715,"role":"AN_JIE_ZHU_BAN"},
                    {"personId":1000000020132500,"role":"SHEN_HE_ZHUAN_YUAN"}]
         })

    headers = {
        "Content-type":"application/json;charset=UTF-8",
        "Connection": "keep-alive",
        "Content-Length": 10000000
    }
    print params

    httpClient = httplib.HTTPConnection("10.10.35.13", 8890, timeout=5)
    httpClient.request("POST", "diandan/commit", params, headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()  # 获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()