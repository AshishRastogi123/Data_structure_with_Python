"""Amstrong number check program
An Armstrong number of n digits is an integer such that the sum of the nth powers of its digits is equal to the number itself.
For example, 153 is an Armstrong number of three digits since 1^3 + 5^3 + 3^3 = 153. """

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