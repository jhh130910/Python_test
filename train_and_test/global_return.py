
def add(a,b):
    ''' global statement  is need  
        函数以外的地方访问变量对象
    '''

    global rrturn    
    rrturn = a + b 

add(1,3)


print (rrturn)

def add_new(a,b):
    '''
    注意，return 返回值带圆括号与不带的区别 ()
    '''
    return a**b

print (add_new(2,4))


def plus(a,b):
    print (a*b + b - a)

plus(4,5)
