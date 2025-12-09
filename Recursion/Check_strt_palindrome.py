"""
Check the string are palindrome or not
"""
n="ashhsa"
left=0
right=len(n)-1

def palindrome(n,left,right):
    if n[left]!=n[right]:
        print(f"{n} is not a palindrome")
        return
        
    elif left>=right:
        print(f"{n} is a palindrome")
        return
    palindrome(n,left+1,right-1)

palindrome(n,left,right)
        

    