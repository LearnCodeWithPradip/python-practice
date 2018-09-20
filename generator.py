

#yield keyword used
def generator():
    yield 1
    yield 2
    yield 3
    yield 4
for i in generator():
    print(i)

#generator object

x = generator()

print(x.__next__());
print(x.__next__());

#using genearator fibonacci number

def fibo(limit):
    
    a,b = 0,1

    while(a < limit):
        yield a
        a , b = b , a+b
x = fibo(5)
print(x.__next__());
print(x.__next__());
print(x.__next__());

#print using for loop
for i in x:
    print(i)


    
