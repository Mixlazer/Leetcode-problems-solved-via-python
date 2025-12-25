class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        counter=0
        for i, el in enumerate(t):
            if s[counter]==el:
                counter+=1
            if len(s)==counter:
                break
        return len(s)==counter
       

                