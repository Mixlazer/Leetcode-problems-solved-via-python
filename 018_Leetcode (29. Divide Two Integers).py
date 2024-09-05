import math
from math import *
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x=0
        if dividend == 0:
            return 0
        if dividend>0 and divisor>0:
            for i in range(dividend):
                x=x+divisor
                if x>dividend:
                    return i
        if dividend>0 and divisor<0:
            for i in range(dividend):
                x=x-divisor
                if x>dividend:
                    return -i
        if dividend<0 and divisor>0:
            for i in range((-1)*dividend):
                x=x+divisor
                if x>(-1)*dividend:
                    return -i
        if dividend<0 and divisor<0:
            for i in range((-1)*dividend):
                x=x-divisor
                if x>(-1)*dividend:
                    return -i

print(Solution().divide(-10, -3))

