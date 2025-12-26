class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, el in enumerate(numbers):
            complement = target - el
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            if el not in seen:
                seen[el] = i

        
        