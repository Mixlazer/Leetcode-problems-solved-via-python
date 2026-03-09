class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        output=str()
        for i in range(1, n+1):
            output+=bin(i)[2:]
        return int(output, 2) % MOD
