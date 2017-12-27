# coding=utf-8
#!/usr/bin/env python
import xlrd,xlwt,os 
from datetime import date,datetime

'''
Create on Sunday April 23 11:02:06 2017
@author:xinxin
@from  :微信公众号:菜鸟学python

#Example :Use Python to parse Excel file 
'''

# 1.实战案例
# 附件有一个input.xlsx文件
# 1).首先xlrd模块去读取文件
# 2).获取input.xlsx文件的sheet1信息
# 3).获取sheet1里面的行数，列数
# 4).获取sheet1里面的每一行，每一列的内容
# 5).获取sheet1里面的指定单元格的内容


def read_excel(filename):
	rdata=xlrd.open_workbook(excel_file)

	#excel sheets 个数
	print('sheets nums:',rdata.nsheets)

	#excel sheets 每个名字
	print('sheets names:',rdata.sheet_names())

	#每个sheet的行数，比如第一个sheet
	sheet1=rdata.sheet_by_index(0)
	print('rows:',sheet1.nrows)
	print('clos',sheet1.ncols)

	#获取sheet1里面的第一行的内容
	print('row1:',sheet1.row(0))

	#获取sheet1里面的第一列的内容
	print('col1:',sheet1.col(0))

	#获取sheet1里面的第二列的内容
	print('col2:',sheet1.col(1))
	print('col2 2-5:',sheet1.col_values(1)[1:5])

	#获取单元格(0,0)
	cell_0_0=sheet1.cell(0,0)
	print('cell_0_0:',cell_0_0)
	print("cell_0_0's ctype:",cell_0_0.ctype)
	print("cell_0_0's value:",cell_0_0.value)


def write_excel(excel_file):
	rdata=xlrd.open_workbook(excel_file)
	sh1=rdata.sheet_by_index(0)
	wbook=xlwt.Workbook()
	wsheet=wbook.add_sheet('new_'+sh1.name)

	#写入第一行,标题栏
	style=xlwt.easyxf('align: vertical center, horizontal center')
	wsheet.write(0,0,u'时间',style)
	wsheet.write(0,1,u'人数1',style)
	wsheet.write(0,2,u'人数2',style)
	wsheet.write(0,3,u'总分',style)

	#写入时间列的数据，需要转化一下数据
	def get_date(cell):
	    if cell.ctype==xlrd.XL_CELL_DATE:
	        date_value = xlrd.xldate_as_tuple(cell.value, rdata.datemode)
	        new_date = date(*date_value[:3]).strftime('%Y/%m/%d')
	        return new_date
	    else:
	        return None

	#从第二行开始写入时间列的数据
	for row in xrange(1,sh1.nrows):
	    new_date=get_date(sh1.cell(row,0))
	    wsheet.write(row,0,new_date,style)


	#计算第二列和第三列的数据和
	nc=sh1.ncols
	for row in xrange(1,sh1.nrows):
	    total=sum(sh1.row_values(row,1))
	    sh1.put_cell(row,nc,xlrd.XL_CELL_NUMBER,total,None)

	#把sheet1里面的第二列,第三列和总分列的数据写入
	for row in xrange(1,sh1.nrows):
	    for col in xrange(1,sh1.ncols):
	        wsheet.write(row,col,sh1.cell_value(row,col),style)

	#写成文件new_data.xls
	try:
	    wbook.save('output.xls')
	except Exception as e:
	    print(e)
	else:
	    print('write excel file successful')


if __name__ == '__main__':
	file_name='input.xls'
	excel_file=os.getcwd()+'\\'+file_name
	print('-'*10+'read excel'+'-'*10)
	read_excel(excel_file)

	print('-'*20)
	write_excel(excel_file)


