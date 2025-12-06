"""
Count the frequency of elements of list m in list n using a hash map.
1. 0<n[i]<10
2. n can have 10^8 elements
3. m can have 10^5 elements
4. Time complexity should be O(n+m)


"""
n=[5,3,2,2,1,5,5,3,4,1,2,5,6,7,8,5,4,3,2,1,10]
m=[10,111,1,9,5,67,2]
lg=[0,1,2,3,4,5,6,7,8,9,10] # since 0<n[i]<10
print(lg)
fs=[0]*11
for i in n:
    fs[i]+=1
hash_map={}
for j in m:
    hash_map[j]=fs[j] if j<=10 else 0
print(hash_map)
