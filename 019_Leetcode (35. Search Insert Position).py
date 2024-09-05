class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        if target not in nums:
            nums.append(target)
            return sorted(nums).index(target)






print(Solution().searchInsert([1,3,4,5], 0))
