class Solution:
    def countSeniors(self, details: list[str]) -> int:
        counter=0
        for i in range(len(details)):
            if int(str(details[i])[11:13])>60:
                counter+=1
        return counter
print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))