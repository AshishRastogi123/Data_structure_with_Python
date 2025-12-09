"""
Check the string are palindrome or not

"""
n="ashha"
left=0
right=len(n)-1
while left<=right:
    if n[left]!=n[right]:
        print(f"{n} is not a palindrome")
        break
    elif left==right or left+1==right:
        print(f"{n} is a palindrome")
        break
    left+=1
    right-=1