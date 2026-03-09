class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = 0
        q = 1
        n = len(nums)
        if n < 4:
            return False
        while p + 1 < n - 2 and nums[p + 1] > nums[p]:
            p += 1
        if p == 0:
            return False
        q = p
        while q + 1 < n - 1 and nums[q + 1] < nums[q]:
            q += 1
        if q == p or q == n - 1:
            return False
        for i in range(q, n - 1):
            if nums[i + 1] <= nums[i]:
                return False
        return True


