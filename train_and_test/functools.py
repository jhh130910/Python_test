from functools import wraps 

def decorator_name(f):
    @wraps(f)
    def decorate(*var,**varss):
        if not can_run:
            return 'func will not run'
        return f(*var,**varss)
    return decorate

@decorator_name
def func():
    ''' 
    decorator_func ...
    '''
    return('func is running ')

can_run = True 
print (func())

can_run = False
print (func())

'''
@wraps 接受一个函数进行装饰，加入了复制函数名称、注释文档、参数列表等功能


'''

'''
example 1 

Authorization 授权检测
from functools import wraps

Logging 日志

'''
