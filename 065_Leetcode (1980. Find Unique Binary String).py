class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        newnums=list()
        for i, el in enumerate(nums):
            newnums.append(int(el, 2))
            newnums.sort()
            if i > 0 and newnums[i] != newnums[i-1]:
                binnum = bin(newnums[i - 1] + 1)[2:]
                diff = len(nums[0]) - len(binnum)
                if "0" * diff + binnum not in nums:
                    return ("0" * diff) + binnum
            else:
                continue
        return "0" * len(nums[0]) if not "0" * len(nums[0]) in nums else "1" * len(nums[0])