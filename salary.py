class Employee:
   '''
docstring ...
'''
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ( "Total Employee %d" % Employee.empCount )
 
   def displayEmployee(self):
      print ( "Name : ", self.name,  ", Salary: ", self.salary )

obj = Employee('jin','2')
obj.displayCount()
obj.displayEmployee()

#print ( obj.__dict__ )
#print ( obj.__doc__ )
#print ( obj.__module__)
class student():    
    grade = ''    
    def __init__(self,n,a,w,g):    
        #调用父类的构函    
       self.grade = g    
        #覆写父类的方法    
    def speak(self):    
       print("%s is speaking: I am %d years old,and I am in grade %d"%(self.name,self.age,self.grade))         
class speaker():    
    topic = ''    
    name = ''    
    def __init__(self,n,t):    
        self.name = n    
        self.topic = t    
    def speak(self):    
        print("I am %s,I am a speaker!My topic is %s"%(self.name,self.topic))    
  
#多重继承    
class sample(speaker,student):    
    a =''    
    def __init__(self,n,a,w,g,t):    
        student.__init__(self,n,a,w,g)    
        speaker.__init__(self,n,t)    
  
test = sample("Tim",25,80,4,"Python")    
test.speak()#方法名同，默认调用的是在括号中排前地父类的方法  
