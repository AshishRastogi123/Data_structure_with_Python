"""
2149. Rearrange Array Elements by Sign

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
"""

class Solution:
    def rearrange_by_sign(self,nums: list[int])->list[int]:
        result=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                result[p]=nums[i]
                p+=2
            elif nums[i]<0:
                result[n]=nums[i]
                n+=2
        return result
        """
        time complexity:O(n)
        space complexity: O(n)
        """


            
    def Brute_force(self,nums: list[int])->list[int]:
        """
       time complexity : o(n+n/2)=O(n)
       space complexity: O(n)/ O(1)
        """
        p=[]
        n=[]
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            elif nums[i]<0:
                n.append(nums[i])
        # for i in range(len(nums)):
        #     if i%2==0:
        #         nums[i]=p[x]
        #         x+=1
        #     else:
        #         nums[i]=n[y]
        #         y+=1 not too much good
        for i in range(len(p)):
            nums[2*i]=p[i]
            nums[2*i+1]=n[i]
        return nums
s=Solution()
nums = [3,1,-2,-5,2,-4]
l=s.Brute_force(nums)
h=s.rearrange_by_sign(nums)
print(h)

