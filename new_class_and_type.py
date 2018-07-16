
class A:       #旧式类
    def __init__(self):
        print ( "classic type." )

class B(object):  #新式类
    def __init__(self):
        print ( "new style type. one" )

__metaclass__ =type
class C:               #新式类
    def __init__(self):
        print ( "new style type. two" )


a=A()
b=B()
c=C()

print ( "class A __class__:%s,type:%s \n"% (a.__class__,type(a)) )
print ( "class B __class__:%s,type:%s \n"% (b.__class__,type(b)) )
print ( "class C __class__:%s,type:%s \n"% (c.__class__,type(c)) )
