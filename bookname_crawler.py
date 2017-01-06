import re, xlwt
import urllib.request

# store all book names from list shown on "douban"
pat = '<div class="name">(.*?)</div>'
data = urllib.request.urlopen("https://read.douban.com/provider/all").read()
nameList = re.compile(pat).findall(str(data, "utf-8"))

'''
Here, data is binary file, we must  convert it into string. there are two approaches:
1) data = str(data, "utf-8")
2) data = data.decode("utf-8")
'''
#print(nameList)

# create excel sheet to save book names
worksheet = xlwt.Workbook() # instantiate class Worksheet under xlwt module
sheet1 = worksheet.add_sheet("sheet1", cell_overwrite_ok=True)

# create style of the sheet
style1 = xlwt.easyxf('font: name Times New Roman, color red')
style2 = xlwt.easyxf('font: name Times New Roman, color blue')

# write item name into sheet1
Item = ["Item Number", "Name" ]
rowNum = 0
columnNum = 0
for item in Item:
        sheet1.write(rowNum, columnNum, item, style1)
        columnNum = columnNum+1

rowNum = rowNum+1 # turn to the next row

for bookname in nameList:
        columnNum = 0
        sheet1.write(rowNum, columnNum, rowNum, style2)
        sheet1.write(rowNum, columnNum+1, bookname, style2)
        rowNum = rowNum+1

worksheet.save("C:/Users/Administrator/Desktop/Bookname_crawler"+".xls")

print("complete writing booknames into excel")

