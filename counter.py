'''counter is a container include in collection moule
syntax = class collections.Counter([iterable-or-mapping])
'''



from collections import Counter 

# Create a list 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))

col_count = Counter(z) 
print(col_count) 
  
col = ['blue','red','yellow','green'] 
  
# Here green is not in col_count  
# so count of green will be zero 
for color in col: 
    print (color, col_count[color]) 
#elements

coun = Counter(A=3,B=2,C=1)
print(coun)

print(list(coun.elements()))
