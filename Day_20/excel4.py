import xlrd
import xlwt
from xlutils.copy import copy
wb_for_read = xlrd.open_workbook("阿里巴巴2020年股票数据.xlsx")
sheet1 = wb_for_read.sheet_by_index(0)
nrows,ncols = sheet1.nrows,sheet1.ncols
wb_for_write =copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows,4,xlwt.Formula(f"average(E2:E{nrows})"))
sheet2.write(nrows, 6, xlwt.Formula(f'sum(G2:G{nrows})'))
wb_for_write.save('阿里巴巴2020年股票数据汇总.xls')