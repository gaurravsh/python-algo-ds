# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            elif c== ')' :
                if len(stack)==0: return False
                t = stack.pop()
                if t!='(': return False
            elif c== '}' :
                if len(stack)==0: return False
                t = stack.pop()
                if t!='{': return False
            else :
                if len(stack)==0: return False
                t = stack.pop()
                if t!='[': return False
        
        return len(stack)==0