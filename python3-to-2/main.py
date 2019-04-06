te=int(input())   
for t in range(te):     
    tot=0
    n=int(input())
    d=[0]*5
    vowel=[0]*32
    for i in range(n):
        stringg=input()
        stringg=set(stringg)
        stringg=list(stringg)
        tot=0
        d=[0]*5
        for j in range(len(stringg)):
            if stringg[j]=='a':
                d[0]=16
            if stringg[j]=='e':
                d[1]=8    
            if stringg[j]=='i':
                d[2]=4
            if stringg[j]=='o':
                d[3]=2    
            if stringg[j]=='u':
                d[4]=1    
        qwe=sum(d) 
        tot=tot+qwe    
        vowel[d[0]|d[1]|d[2]|d[3]|d[4]]=vowel[d[0]|d[1]|d[2]|d[3]|d[4]]+1
    
    count=0
       
    for i in range(32):
        if vowel[i]==0:
            continue
        for j in range(i+1,32):
            if vowel[j]==0:
                continue
            if i|j==31:
                count=count+(vowel[i]*vowel[j])
            
    r=vowel[31]
    
    res=(r*(r-1))/2
    
    summ=count+res
    summ=int(summ)
    print(summ)