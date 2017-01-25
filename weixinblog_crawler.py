import urllib.request
import re

def use_proxy(proxy_addr, url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0')
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        print(len(str(data)))
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    
for i in range(1, 2):
    print(str(i))
    keyword = "python"
    keyword = urllib.request.quote(keyword)
    #url = "http://weixin.sogou.com/weixin?type=2&query="+keyword+"&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=4048&sst0=1485287846128&lkt=7%2C1485287842475%2C1485287846010"
    url = "http://weixin.sogou.com/weixin?query="+keyword+"&_sug_type_=&sut=4048&lkt=7%2C1485287842475%2C1485287846010&_sug_=n&type=2&sst0=1485287846128&page="+str(i)+"&ie=utf8&w=01019900&dr=1"
    print(url)

    proxyAddress = "127.0.0.1:8888"
    data_f = use_proxy(proxyAddress, url).decode()

    ph = 'target="_blank" href="(.*?)"'
    url_blog = re.compile(ph, re.S).findall(data_f)
    print(url_blog)

    for j in range(0, len(url_blog)):
        print("-------blog text "+str(j)+" is being crawling")
        thisUrl = url_blog[j]
        thisUrl = thisUrl.replace("amp;","")
        print(thisUrl)
        try:
            data = use_proxy(proxyAddress, thisUrl)
            file  = open("C:/Users/Administrator/Desktop/blog text/"+"bog text"+str(j)+".html", "wb")
            file.write(data)
            file.close()
            print("-------blog text "+str(j)+" is attained")
        except Exception as e:
            print(e)
