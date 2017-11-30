import urllib
import urllib2
import httplib

class pythonUrl:


    # 全部开放基金
    def request1(appkey, m="GET"):
        url = "http://web.juhe.cn:8080/fund/netdata/all"
        params = {
            "key": appkey,  # APPKEY值

        }
        params = urlencode(params)
        if m == "GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)

        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                print res["result"]
            else:
                print "%s:%s" % (res["error_code"], res["reason"])
        else:
            print "request api error"