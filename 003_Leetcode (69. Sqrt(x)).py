class Solution:
    def mySqrt( x: int) -> int:
        y=[x]
        z=len(str(x))
        f = 1
        for i in range(z, 0, -1):
            f *= i
        if x<10000:
            for i in range(1,x):
                y.append((1/2)*(y[i-1]+(x/y[i-1])))
            return int(y[len(y)-1])
        if x > 10000:
            for i in range(1,x//(f)):
                y.append((1/2)*(y[i-1]+(x/y[i-1])))
            return int(y[len(y)-1])

print(Solution.mySqrt(2147395599))