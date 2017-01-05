import re, xlwt
import urllib.request

# store all book names from list shown on "douban"
pat = '<div class="name">(.*?)</div>'
data = urllib.request.urlopen("https://read.douban.com/provider/all").read()
nameList = re.compile(pat).findall(str(data, "utf-8"))
print(nameList)

# create excel sheet to save book names
worksheet = xlwt.Worksheet() # instantiate class Worksheet under xlwt module
sheet1 = worksheet.add_sheet(sheet1, cell_overwrite_ok=True)

# create style of the sheet
style1 = xlwt.easyxf('fond: name Times New Roman, color red')
style2 = xlwt.easyxf('fond: name Times New Roman, color blue')

# write item name into sheet1
Item = ["Item Nmber", "Name" ]
rowNum = 0
for item in Item
	sheet1.write(0, rowNum, item, style1)
    rowNum = rowNum+1
	


for bookname in namelist
	sheet1.write()
