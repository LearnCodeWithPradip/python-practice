class Test:
    def __init__(self):
        self.x = 100
        self.str = "pradip kolage"

def fuc():
        return Test()

f = fuc()
print(f.x)
print(f.str)

#using tuple
def tuple():
    a = 200
    str1 = "pradip"
    return a ,str1
a,str1 = tuple()
print(a)
print(str1)

#usng list
def list():
    b = 300
    str2 = "kolage"
    return [b,str2]

l = list()
print(l)

#using Dectionary

def dict1():
    d =  dict()
    d['str'] = "pradipkolage"
    d['c'] = 500
    return d
xyz = dict1()
print(xyz)

    
