'''
docstring ...
'''
# 抓取想要的东西
import glob

# collections

import sys      
try:
    directory = sys.argv[1]   
except IndexError:
    sys.exit("Must provide an argument.")

# getpass
getpass.getpass() # 返回用户输入密码
getpass.getuser() # 当前系统用户名称

#2 - 3 导入__future__模块的某些功能，测试新版本的新功能
from __future__ import print_function,division
# collections 1.计数 2.字典有序化 
from collections import Counter
S= 'xxockdd'
count = Counter(S)
count.most_common(5)

from collections import OrderedDict

# pprint 
pprint模块 提供了打印出任何python数据结构类和方法。

# lxml
lxml包用于解析XML和html文件

# 拷贝文件及文件夹操作
import shutil
# random 
import random
'''
random.random()  # 0 - 1
random.randint(2,100)  # 2 - 100
'''

import requests, json, webbrowser,cv2,numpy
import numpy as np
import math
# 
#json：用于字符串和Python数据类型间进行转换
#pickle: 用于python特有的类型和python的数据类型间进行转换
#json提供四个功能：dumps,dump,loads,load
#pickle提供四个功能：dumps,dump,loads,load
'''
pickle可以存储什么类型的数据呢？
所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
由任何原生类型组成的列表，元组，字典和集合。
函数，类，类的实例
'''
import pickle
import json
import os
'''
os.path.basename()
os.path.splitext()
os.path.getsize(filename)
os.system(CMD)
for dirpath, dirname, filenames in os.walk(path)
os.makedirs(folder_name)
os.path.join('dir','file')
os.getcwd()
os.listdir()
os.system()
os.path.split()函数返回一个路径的目录名和文件名
os.path.isfile()和os.path.isdir()
os.path.exists('path')
os.listdir(os.getcwd()) 列举当前路径下文件
os.chdir(dirname):改变工作目录到dirname
os.remove() # 清理
'''
import sys
import re
import time
'''
time.strftime("%Y-%m-%d")
2018-07-01
'''
import 
#============ range ..
for i in range(0,255,2) # start ,end ,step

#=========  file read  seek
seek() 方法用于移动文件读取指针到指定位置
tell():返回文件读取指针的位置
seek()的三种模式：
    （1）f.seek(p,0)  移动当文件第p个字节处，绝对位置
    （2）f.seek(p,1)  移动到相对于当前位置之后的p个字节
    （3）f.seek(p,2)  移动到相对文章尾之后的p个字节

#  while true
while True :
    pass

# '\n'.join(lines)
'\n'.join(objxxx)

#=============== help 1 =====
text = '''
text ...
........
'''
if '-h' in sys.argv or '--h' in sys.argv :
    print ( text )
    sys.exit(0)    

#========== lower()  startswith('xx')
 sys.argv[1].lower().startswith('-c')

#==========   len sys.argv =========
if len(sys.argv) < 2 :
    sys.exit(__doc__)

#========= try .. except  
b=0
try:
    c=a/b
    print c
except ZeroDivisionError,e:
    print e.message
print "done"

#==========  os.path.exists
# 判断文件、文件夹、变量
if not os.path.exists(comic_location):
    os.makedirs(comic_location)
    sys.exit(__doc__)

#=========== def func and with open(file,'wrb') as xxx: 

def count_chars(filename):
    count = {}
    with open(filename) as info:  
        readfile = info.read()
        for character in readfile.upper():
            count[character] = count.get(character, 0) + 1
    return count

def main():
    is_exist=True
    while(is_exist):
        try:
            inputFile = input_func("File Name / (0)exit : ")
            if inputFile == "0":
                break
            print(count_chars(inputFile))
        except FileNotFoundError:
            print("File not found...Try again!")
#==========  enumerate 

def twoSum(nums, target):
    chk_map = {}
    for index, val in enumerate(nums):
      compl = target - val
      if compl in chk_map: 
        indices = [chk_map[compl], index]
        print(indices)
        return [indices]
      else:
        chk_map[val] = index
return False

#=============  睡眠一段时间 
time.sleep(0.2)

#============ 装饰器 =====
#=========== 列表推导式 =======
@timy.timer(ident = 'listcomp', loops = 1) # timy decorator
def listcomprehension(): # the function whose execution time is calculated.
    li = [x for x in range(0,100000,2)]

#============ 写入文件 ======
def write_to_file(filename, txt):
  with open(filename, 'w') as file_object:
      s = file_object.write(txt)
    
if __name__ == '__main__':
    write_to_file('test.txt', 'I am beven')
# try ... except ... finally
try :
   pass
except :
    break
finally :
    # do 

# =====  常见的摘要算法，如MD5，SHA1
import hashlib
md5 = hashlib.md5()
# 文件拆开去验证，结果一样，这个文件内容可以遍历
md5.update('content or text')
print md5.hexdigest()

def md5(fname):
    """ Function to return the MD5 Digest of a file """

    hash_md5 = hashlib.md5()
    with open(fname, "rb") as file_var:
        for chunk in iter(lambda: file_var.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#======  PIL：Python Imaging Library
import PIL
#======  turtle 乌龟画图 
import turtle 
#======= 
import requests
from bs4 import BeautifulSoup
#===== 判断文件夹下某个类型的文件.py .log ...
for files in os.listdir(logsdir):										# Find all the files in the directory
	if files.endswith(".log"):											# Check to ensure the files in the directory end in .log
		files1=files+"."+strftime("%Y-%m-%d")+".zip"		
		os.chdir(logsdir) 												# Change directory to the logsdir
		os.system(zip_program + " " +  files1 +" "+ files)	
		shutil.move(files1, zipdir)									# Move the zipped log files to the zipped_logs directory - 1.2
		os.remove(files)													# Remove the original log files

#=========  string 
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)

#  control words
pass
continue
break
raise

# whiel xx not in xx_obj or not ... 
while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
#=========  __name__ ========
if __name__ == '__main__' :
        pass 
    print ( ' finish ok ... ' )
