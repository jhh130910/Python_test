'''
'''
__author__ = 'jinhh'

class Multiply():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def multiply_two_num(self):
        return self.a * self.b

para_a = input("input a num \n")
para_b = input("input a num \n")

obj_multiply = Multiply(int(para_a),int(para_b))

print (obj_multiply.multiply_two_num())

#  Parent_multiply 继承 Multiply
class Parent_multiply(Multiply):
    pass

obj_parent_multiply = Parent_multiply(3,3)
print (obj_parent_multiply.multiply_two_num())


