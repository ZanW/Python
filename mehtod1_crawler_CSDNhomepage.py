# this application crawls all blogs on home page of http://blog.csdn.net/

import urllib.request
import re

url = "http://blog.csdn.net/"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0")

opener = urllib.request.build_opener()
opener.addheaders = [headers]
try:
    data = opener.open(url).read()
except urllib.error.URLerror as e:
    print(e)
data = data.decode("utf-8", "ignore")

path = 'class="tracking-ad" data-mod="popu_254"><a href="(http://blog.csdn.net/.*?)"'
allurl = re.compile(path).findall(data)
print("the size of crawled data is: "+str(len(allurl)))
print(allurl)

for i in range(0, len(allurl)):
    print("crawling "+str(i))
    # file = "C:/Users/Administrator/Desktop/AllBlogs_ofCSD/"+str(i)+".html"
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        data = opener.open(allurl[i]).read()
        file = open("C:/Users/Administrator/Desktop/AllBlogs_ofCSD/"+str(i)+".html", "wb")
        file.write(data)
        file.close()
        #urllib.request.urlretrieve(allurl[i], file)
    except Exception as e:
        print(e)
    print("the "+ str(i)+"crawling succeed")

