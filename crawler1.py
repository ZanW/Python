import re
import urllib.request
pat = "</em><em>QQ:(.*?)</em></dt>"
data = urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/259").read()
QQ = re.compile(pat).findall( str(data))
print(QQ)
