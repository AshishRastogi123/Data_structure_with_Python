"""
boble sort optimal solution if list is sorted then break the loop
"""

# n=[3,5,1,8,7,2,4,6,0,9,11,10]
n=[1,2,3,4,5,6,7,8,9]
p=len(n)
for i in range(p-2,-1,-1):
    is_swap=False
    for j in range(0,i+1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            is_swap=True
    if is_swap==False:
        break
print(n)

"""
Here the time complexity is : o(n(n+1)/2) =o(n^2) for best / worst and average case
"""