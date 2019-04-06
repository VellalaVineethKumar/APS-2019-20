# cook your dish here
globcount=0
def check(string) : 
    vowels = set("aeiou") 
    s = set({}) 
    for char in string : 
        if char in vowels : 
            s.add(char) 
        else: 
            pass
    if len(s) == len(vowels) : 
        global globcount
        globcount =  globcount+1

import itertools
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    globcount=0
    for _ in range(n):
        arr.append(input())
    people=arr
    list_of_pairs = [check(list(set(str(people[p1] + people[p2])))) for p1 in range(len(people)) for p2 in range(p1+1,len(people))]
    print(globcount)
    
        



##THIS WORKS
