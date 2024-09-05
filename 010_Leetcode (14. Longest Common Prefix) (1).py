class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix={}
        shortest = min(strs, key=len)

        for str in strs:
            prefixstr=[]
            for i in range(len(shortest)):
                if shortest[:(i+1)] == str[:(i+1)]:
                    prefixstr.append(shortest[:(i+1)])
            prefix[str] = prefixstr
        counter = len(prefix[strs[0]])
        shortestprefix=prefix[strs[0]]
        for str in strs:
            if len(prefix[str])<counter:
                counter=len(prefix[str])
                shortestprefix=prefix[str]
        if len(shortestprefix)==0:
            return ""
        else:
            return shortestprefix[-1]

        #print(prefix, shortestprefix, len(shortestprefix))

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
