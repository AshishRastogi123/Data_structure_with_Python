n=[1,4,9,7,29,25,37,40,29,4,9,1,7,25,40,37,11,13,17,19,23,29]
from math import sqrt
for i in range(len(n)):
    if n.count(n[i])>1:
        print(f"Duplicate element found: {n[i]}")
        for j in range(1,sqrt(n[i])+1):
            if n[i]%j==0:
                if j!=1 and j!=n[i]:
                    break