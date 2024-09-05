class Solution:
    def romanToInt(self,s: str) -> int:
        result=0
        dictionary = {'': 0, 'I': 1,'II': 2,'III': 3, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C':100,
                      'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        i = 0
        while i < len(s):
            if i + 1 < len(s) and dictionary[s[i]] < dictionary[s[i + 1]]:
                result += dictionary[s[i]+s[i + 1]]
                i += 2
            else:
                result += dictionary[s[i]]
                i += 1

        return result

print(Solution().romanToInt("IV"))
