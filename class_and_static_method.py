'''
实例化类(类的创建)需要通过调用其构造函数来实例化，python中的实例化会自动调用类的构造方法init(),可以通过指定init方法参数来实例化对象，同时需要注意的是一个类中只能有一个init函数。


迭代器，生成器(yeild)

'''

class TestClass:   #类的定义
    DESCRIPTION = "class introduction"  # 类变量，可直接通过类名调用
    __test = "self_test"  # 属于私有，不可在类外部直接调用以“__”开头
    _single = "self_single"  # 属于私有,不可使用from module import *导入使用

    def __init__(self,name):
        '测试类'        #注释文档
        self.name=name #通过self可以创建类的实例变量
        print ( TestClass.__test )
        print ( TestClass._single )


    def getName(self): #类的成员方法
        return self.name


    def __getName(self): #类的私有方法
        return TestClass._single    

    @staticmethod
    def getsingele():   #类的静态方法
        return TestClass.__test



print ( TestClass.DESCRIPTION )
print ( TestClass.getsingele() )
test=TestClass("huihui")
print ( test.name )

print ( TestClass("OK").name )

print ( test.getName() )
print ( TestClass.getName(test) )

print ( TestClass(test).getName() )
