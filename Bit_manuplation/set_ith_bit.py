class Solution:
    def set_bit(self,a,i):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        b=a | (1 << i)
        return b
    
    def clear_bit(self,a,i):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        b=a & (~(1<<i))
        return b
    def toggle_i_bit(self,a,i):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        b=a ^(1<<i)
        return b
    
    def remove_last_bit(self,a):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        b=a&(a-1)
        return b
    def check_num_is_pow_of_2(self,a):
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if a & (a-1)==0:
            return True
        else:
            return False
s=Solution()
p=s.check_num_is_pow_of_2(16)
print(p)