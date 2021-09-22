# Problem number 704
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums: List[int], l:int, r:int):
            if l==r:
                if nums[l]==target: return l
                else: return -1
            else:
                m=int((l+r)/2)
                if nums[m]==target: return m
                else:
                    a=bs(nums,l,m)
                    b=bs(nums,m+1,r)
                    
                    if a!=-1: return a
                    elif b!=-1: return b
                    else: return -1
        
        
        return bs(nums,0,len(nums)-1)