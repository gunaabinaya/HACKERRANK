s,t=map(int,input().split())
s,t =[int(s),int(t)]
a,b=map(int,input().split())
a,b=[int(a),int(b)]
m,n=map(int,input().split())
m,n=[int(m),int(n)]
apples=list(map(int,input().split()))
organe=list(map(int,input().split()))
c=0
d=0
for i in range(0,m):
    apples[i]=apples[i]+a
    if apples[i]>=s and apples[i]<=t :
        c=c+1
      
        
for j in range(0,n):
    organe[j]=organe[j]+b
    if organe[j]>=s and organe[j]<=t :
        d=d+1
        
print(c)
print(d)
