
#  test permutations and combinations 

import itertools as it

for i in it.combinations('abcd',2):
    print (i)

for j in it.combinations('123456',4):
    print (j)

for k in it.permutations('ABCDEF',2):
    print (k)

for m in it.product('ZXY','1234'):
    print (m)

import itertools

lists = ['a','b','c']

print (list(itertools.permutations(lists,2)))#排列，和顺序有关
print ('='*60)
print (list(itertools.combinations(lists,2)))#组合，和顺序无关
for i in range(1,len(lists)+1):
    print (list(itertools.permutations(lists,2)))#排列，和顺序有关
    print ('='*60)
    print (list(itertools.combinations(lists,2)))#组合，和顺序无关
