import sys
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(30000)
        return str(int(num1) * int(num2))