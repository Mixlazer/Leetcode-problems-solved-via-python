class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearedstr=str()
        for i, el in enumerate(s):
            if el.isalnum()==True:
                clearedstr+=el.lower()
        return clearedstr==clearedstr[::-1]
            