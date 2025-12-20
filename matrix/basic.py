"""
Docstring for matrix.basic
"""
nums=[[5,3,4],[6,7,4],[3,5,3]]
n=len(nums)
for i in range(n):
    for j in range(len(nums[i])):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

print("\n")
for i in range(n):
    for j in range(len(nums[i])):
        if j<=i:
            print(nums[i][j],end=" ")
        else:
            print("*", end=" ")
    print()

print("\n")
for i in range(n):
    for j in range(len(nums[i])):
        if j==i:
            print(nums[i][j],end=" ")
        else:
            print("*", end=" ")
    print()

print("\n")
for i in range(n):
    for j in range(len(nums[i])):
        if  i+j==len(nums)-1: # or j==len(nums[i])-(i+1) 
            print(nums[i][j],end=" ")
        else:
            print("*", end=" ")
    print()

"""
Transpose of the matrixs
"""

nums=[[1,2,3],[3,2,4]]
row=len(nums)
column=len(nums[0])
result=[[0]*row for _ in range(column)]
for i in range(row):
    for j in range(column):
        result[j][i]=nums[i][j]
print(result)