class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=[]
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for str in strs:
                if shortest[:(i+1)] == str[:(i+1)]:
                    prefix.append(shortest[:(i+1)])

        print(prefix)
        if len(strs)==1:
            return strs[0]
        elif shortest == "":
            return ""
        elif len(prefix)== 0:
            return ""
        else:

            for i in range(len(strs)):
                if prefix[0]!=strs[i][0]:
                    return ""
            mostfrequentprefix=max(prefix,key=prefix.count)
            counter=prefix.count(mostfrequentprefix)
            if counter<len(strs):
                return ""
            for i in range(len(prefix)):
                counter = prefix.count(mostfrequentprefix)
                prefix = [j for i, j in enumerate(prefix) if j != mostfrequentprefix]
                if len(prefix)==0:
                    return mostfrequentprefix
                else:
                    mostfrequentprefix1 = max(prefix, key=prefix.count)
                    if prefix.count(mostfrequentprefix1)<counter:
                        return mostfrequentprefix
                    else:
                        mostfrequentprefix=mostfrequentprefix1
            #print(prefix,mostfrequentprefix)

print(Solution().longestCommonPrefix(["abca","aba","aaab"]))
