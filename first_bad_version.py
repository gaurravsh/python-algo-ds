# Problem no 278
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n) -> int:
        l=0
        r=n-1
        while(l<=r):
            m=(l+r)//2
            if isBadVersion(m):
                r=m-1
            else:
                l=m+1
                
        return l