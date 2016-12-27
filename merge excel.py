rowValue = []
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
	table = sheetList[sheetpage]
	sheetRNum = table.nrows
	return sheetRNum
	
# read a file and get all values of its each row
# row_values() returns a slice of the values of the cells in the given row
# sheet_by_name returns an object of the Sheet class
def getFileValue(file, sheetpage):
		fh = open.xls(file)
		sheetList = fh.sheets()
		list_sheetName = fh.sheet_by_name(sheetList[sheetpage])
		sheetRNum = getRowNum(fh, sheetpage)
		for RNum in range(0, sheetRNum):
			 RData = list_sheetName.row_values(RNum)
			 rowValue.append(RData)
	
# read the first expecting file and 	
	
