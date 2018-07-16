
class Name_Class():
    def self(a,b=0,c=True):
        self.name = a
        
    def add_num():
        self.all += self.name

    # ...

obj_NC = Name_Class()

print ( obj_NC )

la = ['name', 'age']
lb = ['charles', 'unknown']

print (dict(zip(la,lb)) )

for index,value in enumerate(la):
    print ( "index is {0}\tvalue is {1}".format( index ,value ) )

for index,value in enumerate(lb):
    print ( "index is {0}\tvalue is {1}".format( index ,value ) )
