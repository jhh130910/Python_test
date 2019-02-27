
list1 = ['a','b','c']
list2 = [ 1, 3, 5 ]

#print (list(map(list1,list2)))

list3 = []
for i in list2:
	list3.append(i**2)

print (list3)

sq = list(map(lambda x:x**2 , list3))

print (sq)
