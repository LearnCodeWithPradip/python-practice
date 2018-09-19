# Enter your code here. Read input from STDIN. Print output to STDOUT

s=int(raw_input(""))
n=int(raw_input(""))
wt=[]
w= raw_input("").split()
w=[int(i) for i in w]
for i in range(0,n):
    if s==w[i]:
        print i 
        break
