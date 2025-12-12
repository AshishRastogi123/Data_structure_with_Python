"""
check an array is sorted or not

"""
n=[3,5,7,9,16,11,13]
p=True
for i in range(len(n)-1):
    if n[i]>n[i+1]:
        p=False
        break
if p:
    print("sorted")
else:
    print("not sorted")