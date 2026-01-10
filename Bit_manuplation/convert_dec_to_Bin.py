class Solution:
    def convert_to_binary(self,nums:int)->str:
        result=""
        while nums>0:
            if nums%2==1:
                result+="1"
            else:
                result+="0"
            nums=nums//2
        result=result[::-1]
        return result
    
    def binary_to_decimal(self,nums:str)->int:
        """
        Time Complexity : O(len(nums))
        Space Complexity: O(1)
        """
        nums=str(nums)
        decimal_number=0
        power=0
        index=len(nums)-1
        while index>=0:
            cal=int(nums[index])*2**power
            decimal_number+=cal
            power+=1
            index-=1
        return decimal_number


s=Solution()

p=s.binary_to_decimal(1101)
print(p)