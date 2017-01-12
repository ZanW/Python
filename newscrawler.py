import urllib.request
import re
url = "http://www.sina.com.cn/"
data = urllib.request.urlopen(url).read()
data = data.decode("utf=8", "ignore")
try:
    pat = 'a target="_blank" href="(http://news.sina.com.cn/.*?)"'
    allurl = re.compile(pat).findall(data)
except urllib.error.URLerror as e:
    print(e)
print(allurl)


for i in range(0, len(allurl)):
    try:
        print(str(i)+" crawl" )
        thisurl = allurl[i]
        file = "C:/Users/Administrator/Desktop/work_newscrawler/" + str(i)+ ".html"
        urllib.request.urlretrieve(thisurl, file)
        print(str(i)+ "crawl succeed")
    except Exception as e:
        print(e)

