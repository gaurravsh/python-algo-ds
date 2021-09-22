# Problem number 859
# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        
        if len(s)<2 : return False
        
        count_mismatch=0
        alpha={}
        fill_alpha = True
        l = list()
        
        for i in range(len(s)):
            if s[i]!=goal[i]:
                count_mismatch +=1
                if count_mismatch>2:
                    return False
                l.append(i)
                
            elif fill_alpha:
                c = alpha.get(s[i])
                if c is None:
                    alpha[s[i]] = 1
                else:
                    fill_alpha = False
            
        if count_mismatch==1: return False
        
        if count_mismatch==0: return (not fill_alpha)
            
        
        if (s[l[0]],s[l[1]]) == (goal[l[1]], goal[l[0]]):
            return True
        else:
            return False