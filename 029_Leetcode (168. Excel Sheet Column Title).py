import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        z=1
        d={}
        for key in range(26):
            d[z] = string.ascii_uppercase[key]
            z+=1
        d[0] = 'Z'

        num= columnNumber
        new = ''
        while num > 0:
            remainder = (num-1) % 26
            num = (num-1) // 26
            new += d[1+remainder]
        return new[::-1]
print(Solution().convertToTitle(28))
