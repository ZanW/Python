import urllib.request

# get search request from BaiDu
keywd = "python"
# note change url from"https" to "http"
url = "http://www.baidu.com/baidu?wd=" + keywd
rq = urllib.request.Request(url)
data = urllib.request.urlopen(rq).read()
file = open("C:/Users/Administrator/Desktop\Get_requeset.html", "wb")
file.write(data)
file.close()

# get search request from BaiDu with chinese
keywd = "人民"
keywd = urllib.request.quote(keywd)
# note change url from"https" to "http"
url = "http://www.baidu.com/baidu?wd=" + keywd
rq = urllib.request.Request(url)
data = urllib.request.urlopen(rq).read()
file = open("C:/Users/Administrator/Desktop\Get_requeset1.html", "wb")
file.write(data)
file.close()

keywd = "java"
url = "http://www.google.com.hk/?gws_rd=ssl#q="+keywd
print(url)
result = urllib.request.Request(url)
data = urllib.request.urlopen(result).read()
file = open("C:/Users/Administrator/Desktop\Get_requeset3.html", "wb")
file.write(data)
file.close()
