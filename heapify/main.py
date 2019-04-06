hlist=[0,3,2,7,9,11,5,6]
print(hlist)

def heapify(hlist,n):
    
    
    for i in range(n//2,0,-1):
        print(i)
        k=i
        v=hlist[i]
        
        h=False # not yet heapify
        
        while(2*k<=n  and not h):
            j=2*k 
            if(j<n):
                #which child is greater
                if(hlist[j+1]>hlist[j]):
                    j=j+1 
            if v>=hlist[j]:
                h=True
            else:
                hlist[k]=hlist[j]
                k=j 
        hlist[k]=v # why it is updated at last?? answer is first checks its child and then checks its child nad then its child until the tree is heapified once the child is heapified we comeoutof the loop and assign this value ie V to appropritate place
        

#heapify(hlist,len(hlist)-1)


#for heapsort swap parent and last node and call heapify in loop
while(n!=0):
    temp=hlist[0] #root node
    hlist[0]=hlist[n-1]
    hlist[n-1]=temp
    heapify(hlist,n-1)
    n=n-1
    
    
    
print(hlist)


c1 and c2 are nodes indipendent
c1=1
c2=2
if(c1 ==1 and c2==1):
    #do you want c3?
    c3==1
    
if(c3==1):
    c4=2
if(c3 and c4):
    do you want 
    c5==1
    

#keep on removing the nodes with indegree =0 and delete that node' gantt chart is implemented using topological sort

