class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        positions=[]
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    positions.append(i)
            result=[positions[0], positions[-1]]
            return result
        else:
            return [-1,-1]
