import urllib.request
import re
import urllib.error


headers  = ("User Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0")

opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)


commentid = "6228219336534345421"
url = "http://coral.qq.com/article/1674900933/comment?commentid=" + commentid + "&reqnum=20&tag=&callback=jQuery112003986352910587363_1485136507216&_=1485136507223"
print(url)

for i in range(0, 5):
    try:
        data = urllib.request.urlopen(url).read().decode()
    except Exception as e:
        print(e)
    patnextpage = '"last":"(.*?)",'
    allnextpage = re.compile(patnextpage).findall(data)[0]
    print(allnextpage)
    patcomment = '"content":"(.*?)",'
    allcomments = re.compile(patcomment).findall(data)
    print(allcomments)
    for j in range(0, len(allcomments)):
        print("------page "+str(i)+" comment "+ str(j)+" is:" + "------")
        print(eval('u"'+allcomments[j]+'"'))
    url =  "https://coral.qq.com/article/1674900933/comment?commentid=" + allnextpage + "&reqnum=20&tag=&callback=jQuery112003986352910587363_1485136507216&_=1485136507223"
    print(url)
