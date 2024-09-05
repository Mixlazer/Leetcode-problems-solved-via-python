class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        isneedleinstr = False
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[0+i:len(needle)+i]==needle:
                isneedleinstr = True
                return i
            print(haystack[0+i:len(needle)+i])
        if isneedleinstr == False:
            return -1

print(Solution().strStr("mississippi","sipp"))