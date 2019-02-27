'''
类由一系列函数对象组成，类中，函数对象称为方法，方法的第一个参数必须为self，代表实例本身（我的理解），当前实例对象可以理解为dict，k为方法名，v为方法

类封装了一系列方法，且可通过一定规则约定方法访问权限

public , protected , private 访问权限
方法名称约定访问权限

normal_name 
_public_name : 语法上是公共的，可以被访问，不要随意访问
__special_name__ 
__private_name  : private name 不能被继承类引用


继承：object base 

多态： class 支持多态，所有method都是动态bind

'''

class Animal(object):  
    def __init__(self, age, color):  
        self.age =  age  
        self.color = color  
  
    def info(self):  
        print ('age = %s, color = %s' %(self.age, self.color) ) 
  
animal = Animal(5, 8)  
animal.info()  
