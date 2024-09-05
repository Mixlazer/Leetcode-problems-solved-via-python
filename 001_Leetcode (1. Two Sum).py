class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if nums[i]<=target:
                for j in range(i, len(nums)):
                    if nums[i]+nums[j]==target and i!=j:
                        return [i, j]

