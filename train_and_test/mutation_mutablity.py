
def add_num(element,List=[]):
    List.append(element)
    return List

print (add_num(1))
print (add_num(2))
print (add_num(3))


def add_num_new(element,List=None):
    if List is None:
        List = []
    List.append(element)
    return List

print (add_num_new(1))
print (add_num_new(2))
print (add_num_new(3))
