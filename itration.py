#using for loop
city = ['pune','mumbai','nagpur','ahmednagar']
for i in city:
    print(i)

#using while loop    
country = ['india','usa','canada','nepal']
x =0
while (x <len(country)):
    print(country[x])
    x +=1

#indexing using range fuction

cars = ['bmw','tata','audi','skoda']
for i in range(len(cars)):
    print(cars[i])
#Enumrate fuction

cars =['bmq','tata','audi','skoda']
for x in enumerate(cars):
    print(x)

# zip fuction(list,list),(dict,dict)

cars = ['bmw','tata','audi']
price = [100000,20000,30000]

for c , p in zip(cars,price):
    print (f'cars:{c} and its price:{p}')

#zip anther way

a ,b = zip(*[('bmw',10000),('tata',20000),('audi',30000)])
print(a)
print(b)

    
