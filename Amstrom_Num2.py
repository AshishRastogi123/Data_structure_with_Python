n=int(input("Enter a number: "))
num=n
nod=len(str(n))
result=0
while num>0:
    lg=num%10
    result+=lg**nod
    num=num//10
if result==n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")