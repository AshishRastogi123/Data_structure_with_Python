"""
write code to sort a list in descending order using selection sort algorithm
"""
n=[3,5,1,8,7,2,4,6,0,9,11,10]
def selection_sort(n):
    p=len(n)
    for i in range(p):
        for j in range(i+1,p):
            if n[j]>n[i]:
                n[i],n[j]=n[j],n[i]
    return n
print(selection_sort(n))