class Solution:
    def superPow(self, a: int,  b: list[int]) -> int:
        power=0
        for i in range(len(b)):
            power=power+b[i]*(10**(len(b)-i-1))
        return pow(a, power)
print(Solution().superPow(a=1, b = [4,3,3,8,5,2]))

