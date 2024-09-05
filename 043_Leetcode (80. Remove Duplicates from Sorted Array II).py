class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums1=list(set(nums))
        for i in nums1:
            counter=0
            for j in nums:
                if j == i:
                    counter+=1
            while counter>2:
                nums.remove(i)
                counter=counter-1
        return len(nums)

        print(nums)
        print(elements)
print(Solution().removeDuplicates([1,1,1,2,2,3]))


