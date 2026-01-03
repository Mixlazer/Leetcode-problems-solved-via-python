import sys
sys.set_int_max_str_digits(100000)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxsum=0
        if len(nums)==sum(nums):
            return len(nums)-1
        elif sum(nums) == 0:
            return 0
        else:
            s=''.join(map(str, nums))
            subarr=s.split(sep='0')
            print(subarr)
        for i, el in enumerate(subarr):
            if i+1>len(subarr)-1:
                continue
            elif el == '' or subarr[i+1] == '':
                if el != '' and int(el)>maxsum:
                    maxsum=int(el)
                if subarr[i+1] != '' and int(subarr[i+1])>maxsum:
                    maxsum=int(subarr[i+1])
                continue
            elif int(el+subarr[i+1])>maxsum:
                maxsum=int(el+subarr[i+1])
            else: continue
        return len(str(maxsum))




        