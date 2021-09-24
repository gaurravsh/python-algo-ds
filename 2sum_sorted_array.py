# Problem number 167
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        
        while l<r:
            a,b = numbers[l],numbers[r]
            if a+b==target: return [l+1,r+1]
            elif a+b>target: r = r-1
            else: l=l+1
        