
def getMoneySpent(keyboards, drives, s):
    # Complete this function
    spent = -1
    
    for i in keyboards:
        for j in drives:
            if(i + j <= s):
                spent = max(spent, i + j)

    return spent
            

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
