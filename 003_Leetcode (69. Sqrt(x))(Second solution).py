class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 4: return 1 if x else 0
        left = 0
        right = x // 2 + 1
        for _ in range(x):
            root = (right + left) // 2

            if root * root <= x and (root + 1) * (root + 1) > x:
                break
            elif root * root > x:
                right = root
            elif root * root <= x and (root + 1) * (root + 1) <= x:
                left = root + 1
        return root

print(Solution.mySqrt(9))