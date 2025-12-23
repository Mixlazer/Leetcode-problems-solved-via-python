class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        outputlist=list()
        templist=list()
        for i, el in enumerate(nums):
            if el+1 not in nums and el-1 not in nums:
                outputlist.append(str(el))
            elif el+1 in nums:
                templist.append(el)
            else:
                outputlist.append(f'{min(templist)}->{el}')
                templist.clear()
        return outputlist