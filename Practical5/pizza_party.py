n=0
# The number of	cuts
p=1
# The number of slices of pizza
while n>=0:
    n=n+1
    p=(n*n+n+2)/2
    #str() converts a number into a string
    print("cut",str(n),",at most",int(p),"pizza slices")
    if p>=64:# Total member of the IBI1 class is 64
       break
     
