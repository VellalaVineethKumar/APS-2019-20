
stringg="abc"
lengg=len(stringg)
subsize= pow(2,lengg)
#if lengg<0 return case

for i in range(subsize):
    for j in range(lengg):
        if(i & 1<<j):
            print(stringg[j],end="")
    print("")