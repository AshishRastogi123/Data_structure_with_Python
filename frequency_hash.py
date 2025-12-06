n=[1,1,2,3,2,3,5,7,4,7,8,9,4,3,2,1,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
hash_map={}
for i in n:
    hash_map[i]=hash_map.get(i,0)+1
print(hash_map)