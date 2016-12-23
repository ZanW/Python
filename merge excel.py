
all_excelfiles = ["","",""]
all_InOneExcel = [""]

# open excel files
def openExcel(file):
	try:
		fh = xlrd.open_workbook(file)
		reture fh
	except Exception as e:
		print("incorrectly file open type: "+e)

# get all sheets in one excel file
# sheets() returens a list of all sheets in the book
def getSheets(fh):
	return fh.sheets()
		
# read the numbers of row in one sheet
def getRowNum(fh, sheetpage):
	sheetList = fh.sheets()
	table = sheetlist
	
	
