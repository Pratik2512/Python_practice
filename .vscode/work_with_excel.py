import xlrd

xl_file = r"C:\Users\prati\Downloads\Book 5.xlsx"

workbook = xlrd.open_workbook(xl_file)
worksheet = workbook.sheet_by_index(0)
print("the value at row 1 and column 2 is :{0}".format(worksheet.cell(1, 2).value))
