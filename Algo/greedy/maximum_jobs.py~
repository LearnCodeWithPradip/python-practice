l=[]
t=[]

n,imp=raw_input("").split()
sum=0
ctr=0
#print n,imp
for i in range(0,int(n)):
    n1,n2=raw_input("").split()
    l.append(n1)
    t.append(n2)
#print l
#print t
for j in range(0,len(t)):
 if int(t[j]):
   ctr=ctr+1

l=[int(i) for i in l]
t=[int(i) for i in t]
  
for i in range( 0,len(l)-1,1):
   for k in range( 0 ,len(l)-i-1, 1 ):
       if ( l[k] < l[k + 1]):
          temp=l[k]
          l[k]=l[k+1]
          l[k+1]=temp
          temp1=t[k]
          t[k]=t[k+1]
          t[k+1]=temp1

#print l
#print t
#print ctr   
ctr2=0
#val=ctr-int(imp)print val
#print "imp is:",imp
a=0
for i in range(0,len(l)):
     if t[i]==0:
             sum=sum+l[i]
     elif(t[i]!=0) and (ctr2<int(imp)):  
              sum=sum+l[i]
              ctr2=ctr2+1
              #print "ctr2 is:",ctr2
     else :
               sum=sum-l[i]
               #print "hi",l[i]
     #print "sum:",sum 
print sum  
