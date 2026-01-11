class Solution:
    def i_th_bit_set_or_not(self,a,i):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if (a & (1<<i))!=0:
            return True
        else:
            return False
        
    def using_right(self,a,i):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if ((a>>i) & 1 )==1:
            return True
        else:
            return False

s=Solution()
p=s.using_right(13,1)
print(p)