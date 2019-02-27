
#!/usr/bin/env
#
# coding:utf-8
# 
# function author date  version 

class Wrapper:
    def __init__(self, obj):
        self.wrapper = obj

    def __getattr__(self, item):
        print("trace:", item)
        return getattr(self.wrapper, item)


if __name__ == '__main__':
    x = Wrapper([1, 2, 3, 4])
    x.append(35)
    x.remove(2)
    print(x.wrapper)  # [1,3,4,35]
    pass

