class Solution:

    def IsBalanced(s: str) -> bool:
        is_balanced = True
        s1 = ''
        for i in range(len(s)):
            if s[i] == 'a' and ('b' in s1) == True:
                is_balanced = False
            s1 = s1 + s[i]
        return is_balanced

    def IsBalanced2(aPos: list, bPos: list) -> bool:
        is_balanced = True
        for i in range(len(aPos)):
            for j in range(len(bPos)):
                if bPos[j]<aPos[i]:
                    is_balanced= False
        return is_balanced
    def minimumDeletions(self, s: str) -> int:
        bcount=0
        acount=0
        aPos=[]
        bPos=[]
        for i in range(len(s)):
            if s[i]=='a':
                aPos.append(i)
            if s[i]=='b':
                bPos.append(i)
        for i in range(len(s)):
            if s[i] == 'b':
                bcount += 1
            else:
                acount = min(acount  + 1, bcount)
        return acount

print(Solution.minimumDeletions('bbaaaaabb'))


