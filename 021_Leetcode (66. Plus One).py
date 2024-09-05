class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        answer=[]
        number="".join(map(str, digits))
        string=str(int(number)+1)
        for i in string:
            answer.append(int(i))
        return answer
print(Solution().plusOne( digits = [1,2,3]))