start=[]
end=[]

n1,n2=raw_input("").split()
sum=0
ctr=0

for i in range(0,int(n1)):
    n3,n4=raw_input("").split()
    start.append(n3)
    end.append(n4)


start=[int(i) for i in start]
end=[int(i) for i in end]
  
for i in range( 0,len(end)-1,1):
   for k in range( 0 ,len(end)-i-1, 1 ):
       if ( end[k] >= end[k + 1]):
          temp=end[k]
          end[k]=end[k+1]
          end[k+1]=temp
          temp1=start[k]
          start[k]=start[k+1]
          start[k+1]=temp1

print start
print end
ctr=1
ind=0
print start[0],"->",end[0],"\n"

for i in range(1,len(start)):
  #for j in range(0,len(end),1):
    if end[ind]<=start[i]:
      ind=i
      print start[i],"->",end[i],"\n"
      ctr=ctr+1
      

print ctr     
