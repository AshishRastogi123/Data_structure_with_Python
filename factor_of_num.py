from math import sqrt
n=int(input("Enter a number: "))
result=[]
for i in range(1,int(sqrt(n))+1):
    if n % i == 0:
        result.append(i)
        if(i!=int(sqrt(n))):
             result.append(int(n//i))
result.sort()
print(result)

    