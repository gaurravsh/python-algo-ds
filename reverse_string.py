# problem 344. Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        l = len(s)

        for i in range(len(s)//2):
            s[i], s[l-1-i] = s[l-1-i], s[i]

        """
        Do not return anything, modify s in-place instead.
        """
        