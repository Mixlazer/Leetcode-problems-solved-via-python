class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        idealrange=range(max(nums)+1)
        if max(nums)==len(nums)-1:
            return max(nums)+1
        for i, el in enumerate(idealrange):
            if nums[i]!=el:
                return el
