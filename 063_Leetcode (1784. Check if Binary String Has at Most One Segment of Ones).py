class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answ=[]
        nums.sort()
        #print(nums)
        for i, el1 in enumerate(nums):
            if el1 > 0:
                break 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right: 
                current_sum = el1 + nums[left] + nums[right]
                if current_sum == 0:
                    answ.append([el1, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return answ

            