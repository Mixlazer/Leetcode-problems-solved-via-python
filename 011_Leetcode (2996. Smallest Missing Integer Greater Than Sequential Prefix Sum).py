class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        thelongestprefix=[]
        prefixes=[]
        previous_number=nums[0]
        current_number=0
        j=0
        #print(len(nums))
        if len(nums)==1:
            return max(nums)+1
        for i in range(len(nums)):
            if i==1 and nums[i]==previous_number+1:
                thelongestprefix.append(nums[i-1])
            if nums[i]==previous_number+1:
                thelongestprefix.append(nums[i])
                #print(thelongestprefix)
            if nums[i]!=previous_number+1 and i!=0:
                #print(nums[i],j, thelongestprefix)
                prefixes.append(list(thelongestprefix))
                thelongestprefix.clear()
                j=j+1
            previous_number = nums[i]
        prefixes.append(list(thelongestprefix))
        prefixes.append([nums[0]])
        if max(prefixes, key=len)==[]:
            prefixes.append([max(nums)])
        #print(max(nums))
        #print(sum(max(prefixes, key=len)))
        if sum(max(prefixes, key=len)) not in nums:
            return sum(max(prefixes, key=len))
        else:
            for i in range(sum(max(prefixes, key=len)),sum(max(prefixes, key=len))*2):
                if(i not in nums):
                    return i




print(Solution().missingInteger([1,2,3,2,5]))
