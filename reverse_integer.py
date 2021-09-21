# Problem Numer 7
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:    
        abs_x = abs(x)
        is_neg = x<0
        
        a = abs_x%10
        b = int(abs_x/10)
        while b>0:
            a = a*10 + b%10
            b = int(b/10)
        
        if is_neg:
            a = a*-1
        
        lower = pow(2,31) * -1
        upper = pow(2,31) - 1
        
        if a<lower or a>upper:
            return 0
        else:
            return a