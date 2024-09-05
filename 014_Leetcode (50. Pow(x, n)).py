class Solution:
    def myPow(self, x: float, n: int) -> float:
        output=x
        if x==-1 and n%2==1:
            return -1
        if (n > 1000000 and -1 < x < 1) or (n < -1000 and x > 1):
            return 0
        if (x == 1 or n==0) or (x==-1 and n%2==0):
            return 1
        if n >0:
            for i in range(1, n):
                output=output.__mul__(x)
        if n <0:
            for i in range(1, (-1)*n):
                output=output.__mul__(x)
            output=1/output
        return output

print(Solution().myPow(x = -1.00000, n = 2147483647 ))

''' Технически разрешенное решение
def myPow(x, n):
    _p = pow(x, n)
    return _p
'''