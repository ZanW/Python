import urllib.request
import urllib.parse

url = "http://www.iqianyue.com/mypost/"
myInformation = urllib.parse.urlencode(
{
"name":"yipengzan@hotmail.com",
"pass":"1234"}
).encode("utf-8")
request = urllib.request.Request(url, myInformation)
data = urllib.request.urlopen(request).read()

fq = open("C:/Users/Administrator/Desktop/get_test.html", "wb")
fq.write(data)
fq.close()
