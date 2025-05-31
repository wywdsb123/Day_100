"""wang

打开EXCEL.并用循环语言进行读取内容
"""
import xlrd
wb= xlrd.open_workbook("阿里巴巴2020年股票数据.xlsx")
sheetnames =wb.sheet_names()
print(sheetnames)

sheet = wb.sheet_by_name(sheetnames[0])
print(sheet.nrows,sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        if row >0:
            if col==0:
                value = xlrd.xldate_as_tuple(value,0)
                value = f"{value[0]}year{value[1]}month{value[2]}"
            else :
                value =f"{value:.2f}"
        print(value, end='\t')
    print()
last_cell_type =sheet.cell_type(sheet.nrows-1,sheet.ncols-1)
print(last_cell_type)
print(sheet.row_values(0))
print(sheet.row_slice(3,0,5))