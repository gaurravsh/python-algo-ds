# Problem number 35
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while l<r:
            m = l + (r-l)//2
            if nums[m]==target: return m
            elif nums[m]>target : r=m
            else: l=m+1
                
        if nums[l]==target: return l
        elif nums[l]<target: return l+1
        else: return l