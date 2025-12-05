n=int(input("Enter a number:"))
num=n
count=0
result=0
while num>0:
    count+=1
    num=num//10
num=n
while num>0:
    lg=num%10
    result+=lg**count
    num=num//10
if result==n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
