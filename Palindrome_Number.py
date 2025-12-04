n=int(input("Enter a number: "))
num=n
result=0
while num>0:
    lg=num%10
    result=result*10 +lg
    num=num//10
if result==n:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")