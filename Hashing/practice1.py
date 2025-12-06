"""

Count the frequency of elements of list m in list n using a hash map.
1. 0<n[i]<10
2. n can have 10^8 elements
3. m can have 10^5 elements
4. Time complexity should be O(n+m)

solution using brute force approach with O(n*m) time complexity


"""

n=[5,3,2,2,1,5,5,3,4,1,2,5,6,7,8,5,4,3,2,1,10]
m=[10,111,1,9,5,67,2]
hash_map={}
for i in m:
    count=0
    for j in n:
        if i==j:
            count+=1
    hash_map[i]=count
print(hash_map)