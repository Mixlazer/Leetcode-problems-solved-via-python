class Solution:
    def reverse(self, x: int) -> int:
        y=int(str(abs(x))[::-1])
        if x<0:
            y=y*-1
        if y<-2**31 or y>2**31-1:
            return 0
        return y
print(Solution().reverse(-123))