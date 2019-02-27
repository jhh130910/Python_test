from collections import defaultdict
from collections import Counter 
from collections import deque  
from collections import namedtuple 
from enum import Enum 

'''
defaultdict 与dict类型不同，需要检查key是否存在
对一个字典中键进行嵌套赋值时，如果键不存在就会触发keyError异常，defaultdict允许我们用一个聪明的方式绕过这个问题

'''

colours = (('A','red'),('B','yellow'),('A','black')) 

favourite = defaultdict(list)

for name,num in colours:
    favourite[name].append(num)

#print (favourite)

tree = lambda : defaultdict(tree)
dict_temp = tree()
dict_temp['colours']['favourite'] = 'green'

import json

#print ( json.dumps(dict_temp))

favs = Counter( name for name , colour in colours )
print (favs)

with open('file.count','rb' ) as f:
    line_count = Counter(f)
print (line_count)

'''
deque 提供双端队列，可以从头、尾两端添加或者删除元素
'''
# 创建deque对象
d = deque()
d.append('1')
d.append(2)

print (d.pop())
print (len(d))
print (d.popleft())

# deque(range(5))   deque(maxlen=30)
#  maxlen : 限制列表的大小，超出限制，数据会从另一端挤出去
#  d.extend([3,4,5])  d.extendleft([list])

'''
元组是不可变的列表
namedtuples 是把元组变成一个针对简单任务的容器，不可变，单可以像访问字典一样使用
命名元组（namedtuple）有两个必须的参数，元组名称和字段名称
namedtuple 每个实例没有对象字典，很轻量，与普通元组比较，不需要更多内存，比字典更快。
属性值不可变
使用命名元组让代码自文档，（看着就是文档，其实是代码，我的理解）
'''

animal = namedtuple('Animal','name age types')
animal_print = animal(name='name',age=2, types='cat')

print (animal_print)
print (animal_print.name)
print (animal_print._asdict())


'''
枚举对象  enum  Enums（枚举类型，组织各种东西）

'''
class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
# Species(1)  Species['cat'] Species.cat
cat = Species.cat
print (cat)

# enumerate : 枚举，内置函数
# 运行遍历数据并自动计数
list_test = ['a','b','a',1,1,1,3,4,]
for counter, value in enumerate(list_test,2):
        print (counter,value)

counter_list = list(enumerate(list_test,2))
print (counter_list)

