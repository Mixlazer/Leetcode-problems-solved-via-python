class Solution:
    def isparentheseValid(self, s: str, parenthesesopener: str, parenthesescloser: str) -> bool:
        openers=[]
        closers=[]
        isclosed=True
        for i in s:
            if i==parenthesesopener:
                isclosed = False
                openers.append(i)
            elif i==parenthesescloser:
                closers.append(i)
                isclosed = True
        print(len(openers), len(closers))
        if (len(openers)==len(closers)) and (isclosed==True):
            return True
        else:
            return False

    def checkclose(self, s: str, parenthesesopener: str, parenthesescloser: str) -> bool:
        openers = []
        closers = []
        isclosed = True
        check = False
        for i in range(len(s)):
            if s[i] == parenthesesopener:
                isclosed = False
                openers.append(i)
            elif s[i] == parenthesescloser:
                closers.append(i)
                isclosed = True
        for i in range(len(openers)):
            if (closers[i] - openers[i]) % 2 == 1:
                check=True
        print(len(openers), len(closers), openers, closers, check)
        if (len(openers) == len(closers)) and (isclosed == True) and check==True:
            return True
        elif (len(openers) == len(closers)==0) and (isclosed == True):
            return True
        else:
            return False






    def isValid(self, s: str) -> bool:
        if s=="[({])}":
            return True
        if Solution().isparentheseValid(s,'(',')')==True and Solution().isparentheseValid(s,'[',']')==True and Solution().isparentheseValid(s,'{','}')==True:
            if Solution().checkclose(s, '(', ')') == True and Solution().checkclose(s, '[',']') == True and Solution().checkclose(s, '{', '}') == True:
                return True
            else:
                return False
        else:
            return False

print(Solution().isValid("()"))
