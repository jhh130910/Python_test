
# coding: UTF-8 
# 
# 模块自测
# 
import sys
import os

print 'file names is :' + sys.argv[0]

if len(sys.argv)> 1:
	print 'more than one argv'

else :
	print 'no argv exist '

print sys.getdefaultencoding()

#print sys.path

print sys.platform

##  decorator 


def test(a,b):
	pass 
	
