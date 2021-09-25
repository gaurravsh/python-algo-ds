# problem number 977
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [None] * n
        
        l=0
        r=n-1
        
        for i in range(n):
            a,b = nums[l]**2,nums[r]**2
            if a>=b:
                res[n-1-i]=a
                l=l+1
            else:
                res[n-1-i]=b
                r=r-1
                
        return res