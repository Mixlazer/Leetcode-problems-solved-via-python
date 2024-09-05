class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        print('массив',nums)
        print('длина массива',len(nums))
        startlen=len(nums)
        for i in range(startlen):
            print('член массива',nums[i])
            if nums[i]!=val:
                print('не вхождение val', nums[i])
                nums.append(nums[i])
        del nums[:startlen]
        return len(nums)

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
