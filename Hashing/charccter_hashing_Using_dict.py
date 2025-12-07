"""
charccter_hashing
s="aaazysbchcbdjhldsbclas"
q=["a","q","j","y","c","l"]
constraints:
'a'<=s[i]<='z'
"""
s="aaazySMMAKSHUchcbdjhlAdsbclas"
q=["a","q","j","y","c","l",'A']
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1   
wanted_freq={char:freq.get(char,0) for char in q}
print(wanted_freq)
