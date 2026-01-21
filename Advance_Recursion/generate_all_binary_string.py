"""
Generate all binary strings
Given an integer n. You need to generate all the binary strings of n characters representing bits.

Note: Return the strings in  ascending order.
before:
Input: n = 3
Output: [000, 001, 010, 100, 101]

Now question
Input: n = 3
Output: [000, 001, 010, 011, 100, 101, 110, 111]
Explanation: As each position can be either 0 or 1, the total possible combinations are 8.
"""
class Solution:

    def solve(self,index,flag,numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.solve(index+1,True,numbers,result)
        if flag==True:
            numbers[index]="1"
            self.solve(index+1,False,numbers,result)
            numbers[index]="0"


    def generate_all_binary_string(self,n):
        """
        Time complexity : (2**n)
        Space complexity : O(n)
        """
        numbers=["0"]*n
        result=[]
        self.solve(0,True,numbers,result)
        return result
    
    def gfgbackward(self,index,flag,numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.gfgbackward(index+1,True,numbers,result)
        numbers[index]="1"
        self.gfgbackward(index+1,False,numbers,result)
        
    def binstr(self, n):
        """
    Time complexity : (2**n)
    Space complexity : O(n)
    """
        numbers=["0"]*n
        result=[]
        self.gfgbackward(0,True,numbers,result)
        return result
        


s=Solution()
n=3
p=s.binstr(n)
print(p)