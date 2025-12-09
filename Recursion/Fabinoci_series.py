"""
got the number accross the fabnoci series
"""
n=int(input("Enter a Number"))

p=[]
k=0
def fabinoci(n,k,p):
    if n==-1:
        l=p[k-1]
        print(l)
        return 1
    if k==0:
        p.append(0)
    elif k==1:
        p.append(1)
        
    else:
        p.append(p[k-1]+p[k-2])
        print(p)
        print(f"{k} number")
    
    fabinoci(n-1,k+1,p)
fabinoci(n,k,p)