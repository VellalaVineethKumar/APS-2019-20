arr = []
local=[]
local2=[]

def check(numbers):
    for x in numbers:
        if(x>0):
            local.append(x)
        else:
            local2.append(x)
    if(len(local)==len(local2)):
        return len(local)
    
    
    
t=int(input())

for _ in range(t):
    n=int(input())
    numbers = list(map(int, input().split()))
    x=check(numbers)
    print(x x)
    
    