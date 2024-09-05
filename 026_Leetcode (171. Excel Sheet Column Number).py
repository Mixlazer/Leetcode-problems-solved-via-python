import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = dict.fromkeys(string.ascii_uppercase)
        z=1
        for key in d.keys():
            d[key]=z
            z+=1
        answer=0
        for i in range(len(columnTitle))[::-1]:
            answer=d[columnTitle[i]]*26**(len(columnTitle)-i-1)+answer
        return answer
print(Solution().titleToNumber("A"))
