import urllib.request
import urllib.error

# without header setting, crawler is not able to get the data from intented webpage
try:
    data = urllib.request.urlopen("http://blog.csdn.net/u011167358/article/details/54233186").read()
    len(data)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)

fh = open("C:/Users/Administrator/Desktop/csdnWithoutHeader.html", "wb")
try:
    fh.write(data)
except Exception as e:
    print(e)
    print("for csdn without adding headers")
fh.close()

# adding headers makes crawler work like a browser

url = "http://blog.csdn.net/u011167358/article/details/54233186"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data1 = opener.open(url).read()
fh = open("C:/Users/Administrator/Desktop/csdnWithHeader.html", "wb")
fh.write(data1)
fh.close()
