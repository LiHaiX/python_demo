


url = "http://www.example.com"
body_value = {"package": "com.tencent.lian","version_code": "66" }
register_openers()
datagen, re_headers = multipart_encode(body_value)
request = urllib2.Request(url, datagen, re_headers)
# 如果有请求头数据，则添加请求头
request .add_header(keys, headers[keys])
result = urllib2.urlopen(request ).read()