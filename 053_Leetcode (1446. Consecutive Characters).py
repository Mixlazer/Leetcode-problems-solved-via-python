class Solution:
    def maxPower(self, s: str) -> int:
        maxchar=1
        counter=1
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                counter+=1
                maxchar = max(maxchar, counter)
            else:
                counter=1
        return maxchar


           

                  