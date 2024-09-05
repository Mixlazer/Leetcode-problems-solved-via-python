class Solution:
    def repeatcheck(s: str) -> bool:
        if len(set(s))==len(s):
            return True
        else:
            return False
    def lengthOfLongestSubstring(self, s: str) -> int:
        been=set()
        counter=0
        counterarr=[0]
        checklen=0
        while checklen<=len(set(s)):
            for i in range(len(s)-checklen):
                if Solution.repeatcheck(s[i:i+checklen+1]) == True:
                    counterarr.append(len(s[i:i+checklen+1]))
            checklen+=1
        return max(counterarr)
print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))