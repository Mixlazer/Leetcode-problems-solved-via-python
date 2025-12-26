class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda num: pow(num, 2), nums))

        