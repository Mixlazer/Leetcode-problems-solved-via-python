class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums1=list(set(nums))+list(set(nums))
        C = []
        for item in nums:
            try:
                nums1.remove(item)
            except ValueError:
                C.append(item)
        return nums1[0]
print(Solution().singleNumber([2,2,1]))
