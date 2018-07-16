# coding: utf-8

import numpy

class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print ("type:", r'type')
        print ("value:", value )
        print ("trace:", trace )

    def do_something(self):
        bar = 1/0
        return bar + 10

#1、类Sample被实例化后，调用__enter__()方法，将返回值赋给as后的变量sample
#2、with语句下的语句sample.do_something()被执行
#3、语句执行完或者是出现异常时调用__exit__()方法        
