"""
Count the frequency of elements of list m in list n using a hash map.
2. n can have 10^8 elements
3. m can have 10^5 elements
4. Time complexity should be O(n+m)


"""
n = [5,3,2,2,1,5,5,3,4,1,2,5,6,7,8,5,4,3,2,1,10,33,134]
m = [10,111,1,9,5,67,2,33,134]

freq = {}

for num in n:
    freq[num] = freq.get(num, 0) + 1

wanted_freq = {num: freq.get(num, 0) for num in m}
print(wanted_freq)