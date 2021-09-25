# problem 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0: return
        n=len(nums)
        
        for counter in range(k):
            temp=nums[n-1]
            for i in range(n-2,-1,-1):
                nums[i+1],nums[i]=nums[i],nums[i+1]
            nums[0]=temp