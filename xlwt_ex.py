"""
    python可以使用xlrd读excel，使用xlwt写excel，但是如果要把数据写入已存在的excel，需要另外一个库xlutils配合使用.

    大概思路：
    
    1、用xlrd.open_workbook打开已有的xsl文件
    注意添加参数formatting_info=True，得以保存之前数据的格式
    2、然后用，from xlutils.copy import copy;，之后的copy去从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
    3、然后对于xlwt的Workbook变量，就是正常的：
    通过get_sheet去获得对应的sheet，拿到sheet变量后，就可以往sheet中，写入新的数据
    4、写完新数据后，最终save保存
    




"""
import xlrd  
import os  
from xlutils.copy import copy  
from xlwt import Style  
  
def writeExcel(row, col, str, styl=Style.default_style):  
    rb = xlrd.open_workbook(file, formatting_info=True)  
    wb = copy(rb)  
    ws = wb.get_sheet(0)  
    ws.write(row, col, str, styl)  
    wb.save(file)  
  
style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center');  
writeExcel(1, 1, 'hello world', style)  