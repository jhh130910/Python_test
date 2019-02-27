# property：标示属性的装饰器

class C:
    def __init__(self):
        self._name = ''
    @property 
    def name(self):
        ''' name property '''
        return self._name
    @name.setter
    def name(self,value):
        if value is None:
            raise ValueError('name can\'t be None')
        else:
            self._name = value

c = C()
print (c.name)
c.name = 'name'
print (c.name)
#c.name = None

# classmethod：标示方法为类方法的装饰器
class B:
    @classmethod
    def B_func(cls,arg1):
        print (cls)
        print (arg1)
B.B_func('class object call class method')
b = B()
b.B_func('example object call class method')

# staticmethod：标示方法为静态方法的装饰器
# 使用装饰器定义静态方法
class Student(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def sayHello(lang):
        print(lang)
        if lang == 'en':
            print('Welcome!')
        else:
            print('你好！')

Student.sayHello('en') #类调用,'en'传给了lang参数
b = Student('Kim')
b.sayHello('zh')  #类实例对象调用,'zh'传给了lang参数
