import urllib.request
import re

for i in range(1,2):
    pagenumber = str(i)
    url = "http://www.58pic.com/shouye/632/id-"+pagenumber+".html"
    print(url)
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        #data = urllib.request.quote(data)
        path = '<a class="thumb-box".*?src1="(.*?).jpg!qt226" width="226"'
        picUrl = re.compile(path).findall(data)
        print(picUrl)
    except Exception as e:
        print(e)
    for j in range(len(picUrl)):
        print("picture "+str(j)+" is under crawling")
        try:
            file = "C:/Users/Administrator/Desktop/pic_crawler/"+str(j)+".jpg"
            pic = picUrl[j]+"_1024.jpg"
            urllib.request.urlretrieve(pic, file)
        except urllib.error.URLError as e:
            if hasattr(e, code):
                print(e.code)
            if hasattr(e, reason):
                print(e.reason)
        print("picture "+str(j)+" crawling succeed!")
