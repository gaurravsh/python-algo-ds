# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return
        
        max2 = n-1
        max1 = m-1        
        write = m+n-1
        
        while max2>=0 and max1>=0:
            if nums2[max2]>nums1[max1]:
                nums1[write] = nums2[max2]
                max2 = max2-1
            else:
                nums1[write] = nums1[max1]
                max1 = max1-1
            write=write-1
            
        while max2>=0:
            nums1[write]=nums2[max2]
            write=write-1
            max2=max2-1
        