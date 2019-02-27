
def argv_Test(argv1,*var):
	''' 
Usage :  some_func(fargs, *args, **kwargs )

Python有个特性叫做文档字符串，即DocString，这个特性可以让你的程序文档更加清晰易懂，在python的系统文件里，也都在使用这个特性。因此推荐每个Python爱好者都使用它。
DocString是有自己的格式的。一般是放在自己函数定义的第一行，用‘’符号指示，在这‘’里面添加函数功能说明就可以了。这个说明可以使用.__doc__（注意前后都是双_）属性，将DocString特性print打印出来。
'''

	print (argv1)
	for para in var:
		print ("other is ", para)
a1 ='a1'
a2 ='a2'
a3 ='a3'
a4 ='a4'
argv_Test(a1,a2,a3,a4)

def kw(**kv):
	for k,v in kv.items():
		print ("{1} --- {0}".format(k,v))

kw(k='v')

def test_args_kwargs(a1,a2,a3):
	print ('a1',a1)
	print ('a2',a2)
	print ('a3',a3)
#args = ('a',1,2)
kwargs= {'b1':1,'b2':2,'b3':'abc'}
#test_args_kwargs(*args)
test_args_kwargs(*kwargs)

''' 
Usage :  some_func(fargs, *args, **kwargs )
'''

