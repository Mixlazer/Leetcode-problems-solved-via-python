class Solution:
    def removeDuplicates(self, nums: list[int]):
        dictofelements={}
        for i in nums:
            dictofelements[i]=True
        nums=list(dictofelements.keys())
        return len(list(dictofelements.keys()))

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])),