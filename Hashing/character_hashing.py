"""
charccter_hashing
s="aaazysbchcbdjhldsbclas"
q=["a","q","j","y","c","l"]
constraints:
'a'<=s[i]<='z'
"""
s="aaazysbchcbdjhldsbclas"
q=["a","q","j","y","c","l"]
hash_map={}
for char in s:
    ascii_val=ord(char)-ord('a')
    hash_map[ascii_val]=hash_map.get(ascii_val,0)+1   
wanted_freq={char:hash_map.get(ord(char)-ord('a'),0) for char in q}
print(wanted_freq)