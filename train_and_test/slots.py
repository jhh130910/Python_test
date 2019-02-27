
'''
__slots__ : magic method 
python中，类都有实例属性，默认用字典保存对象的实例属性，允许运行时设置任意新属性
缺点：浪费内存
__slots__ 告诉python不使用字典，而且只给一个固定集合的属性分配空间

'''

class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

class MyNewClass(object):
    __slots__ = ['name','identifier']
    
    def __init__(self , name , identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()


'''
内存减轻负担，内存占用率减少约一半

'''
