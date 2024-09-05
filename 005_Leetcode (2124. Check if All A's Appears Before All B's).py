class Solution:
    def checkString(self, s: str) -> bool:
        aPos = []
        bPos = []
        is_before=True
        for i in range(len(s)):
            if s[i] == 'a':
                aPos.append(i)
            if s[i] == 'b':
                bPos.append(i)
        for i in range(len(aPos)):
            for j in range(len(bPos)):
                if bPos[j]<aPos[i]:
                    is_before= False
        return is_before

print(Solution.checkString("bbb"))
