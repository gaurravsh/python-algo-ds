# Problem Number 69
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        l:int = 1
        r:int = x
        m:int = (l+r)//2
            
        while not m*m<=x<(m+1)**2:
            if m*m<x:
                l=m
                m=(l+r)//2
            elif m*m>x:
                r=m
                m=(l+r)//2
            else:
                return m
            # print('l = {}, r = {}, m = {}'.format(l,m,r))
        return m