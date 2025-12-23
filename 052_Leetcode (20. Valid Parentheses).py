class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=s[0]
        pairs={')':'(',']':'[','}':'{',}
        openers={'(','{','['}
        for i, el in enumerate(s[1:]):
            if el in openers:
                stack+=el
            elif len(stack)>0 and stack[-1] == pairs[el]:
                stack=stack[:-1]
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False

           

                  