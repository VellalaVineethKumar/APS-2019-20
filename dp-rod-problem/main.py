#Dp solution on ROD problem
rc=[]

n=7 # length of 
#we will have to check three conditions
#i=2 j=i//2
# 1) if a[i] is max this is checked because j run till i//2 hence  j can take multiplke values and in the next iteration the value may be updated
# 2) if j*(i-j) is max this indicates if we are at number 5, 1*(5-1) half*half-1 is max normally when we are dividong it into two parts
# 3) if j*RC[i-j] is max
# which is the max that value will be filled in the array