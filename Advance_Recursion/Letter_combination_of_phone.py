"""
17. Letter Combinations of a Phone Number

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""
class Solution:
    def comibination_letter(self,digit):
        """
        Time Complexity : O(4^n)
        Space Complexity : O(n)
        """
        if not digit:
            return
        result=[]
        hash_map={}
        idx=97

        for i in range(2,10):
            subset=[]
            if i==7 or i==9:
                p=4
            else:
                p=3
            for j in range(p):
                subset.append(chr(idx))
                idx+=1
            hash_map[str(i)]=subset

        self.solve(0,[],digit,hash_map,result)
        
        return result
    
    def solve(self,index,subset,digit,hash_map,result):
        if index==len(digit):
            result.append("".join(subset))
            return 
        
        letters=hash_map[digit[index]]
        for i in letters:
            subset.append(i)
            self.solve(index+1,subset,digit,hash_map,result)
            subset.pop()
    

s=Solution()
digit="46"
print(s.comibination_letter(digit))