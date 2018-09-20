class Test:
    def __init__(self,limit):
        self.limit = limit
    def __iter__(self):
        self.x = 5
        return self
    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x += 1
        return x

for i in Test(15):
    print(i)

    
# Sample built-in iterators 
  
# Iterating over a list 
print("List Iteration") 
l = ["pradip", "appasaheb", "kolage"] 
for i in l: 
    print(i) 
      
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("kolage", "pradip", "kolage") 
for i in t: 
    print(i) 
      
# Iterating over a String 
print("\nString Iteration")     
s = "pradip"
for i in s : 
    print(i) 
      
# Iterating over dictionary 
print("\nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s  %d" %(i, d[i])) 

