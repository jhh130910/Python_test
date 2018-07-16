
import pprint 
import subprocess  

my_str = "python make_SampleInfo_file.py -fc s4 -add_index yes"

subprocess.call(my_str)

'''

在处理excel数据时发现了xlwt的局限性–不能写入超过65535行、256列的数据（因为它只支持Excel 2003及之前的版本，在这些版本的Excel中行数和列数有此限制），这对于实际应用还是不够的。为此经过一番寻找发现了一个支持07/10/13版本Excel的openpyxl，虽然功能很强大，但是操作起来感觉没有xlwt方便
工作簿(Workbook)
选择工作表(sheets)
单元格(cell)
pyexcel-xls
整个excel文件，转化为一个字典结构：每个key就是一个子表（Sheet）
每个子表（Sheet），转化为一个二维数组：分别为行和列。
版本 pyexcel-xls 0.2.3
整个excel文件，转化为一个OrderedDict (有序字典)结构：每个key就是一个子表（Sheet）。
每个子表（Sheet），转化为一个列表结构：很像二维数组，第一层列表为行（Row），行的下标为列（Column），对应的值为单元格的值。编码为 unicode
注意，excel文件名（就是那个xls或者xlsx文件），尽量不要用中文，如果您要使用中文，请转化为unicode编码，如：
xls_data = get_data(unicode(r"测试用的名字.xlsx", "utf-8"))

'''
