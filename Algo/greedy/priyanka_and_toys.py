n=int(raw_input(""))
wt=[]
w= raw_input("").split()
w=[int(i) for i in w]c
tr=1
ind=0
w=sorted(w)
#print w
for i in range(1,len(w)):
    if w[i] not in range(w[ind],w[ind]+5)  :
       ind=i
       ctr=ctr+1

print ctr       

