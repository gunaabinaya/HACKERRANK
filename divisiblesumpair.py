n,k=map(int, input().split())
s=[]
c=0
s=list(map(int, input().split()))
for i in range (0,n):
    for j in range(i+1,n):
        if (s[i]+s[j])%k==0:
            c=c+1    
print(c)
    
