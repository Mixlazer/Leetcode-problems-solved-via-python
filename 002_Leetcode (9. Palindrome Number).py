class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        forward = [int(y) for y in str(x)]
        backward=forward[::-1]
        if forward==backward:
            return True
        else:
            return False
print(Solution().isPalindrome(1100))