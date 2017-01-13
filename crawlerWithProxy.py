import urllib.request
import types

url = "http://www.baidu.com"
proxyAddr = "125.88.74.122:83"

def url_proxy(url, proxyAddr):
    proxy = urllib.request.ProxyHandler({"http" : proxyAddr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read()
    return data

data1 = url_proxy(url, proxyAddr)
s = type(data1)
print(str(s))
print(str(len(data1)))
file = open("C:/Users/Administrator/Desktop/crawlerWithProxy"+".html", "wb")
file.write(data1)
file.close()



