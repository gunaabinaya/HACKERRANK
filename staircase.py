n=int(input())
for i in range(0,n):
    for s in range(n-1-i,0,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("#",end="")
    print()
