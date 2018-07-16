
'''  args kwargs test '''

class X__():
	
	def __init__(sle,*args):
		sle.args = args

	def every(sle):
		ls = []
		for i in sle.args:
			ls.append(i)	
		return ls
obj = X__(1,2,3,4)
print ( obj.every() )
