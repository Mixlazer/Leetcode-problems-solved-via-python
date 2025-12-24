class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter=0
        for i, el in enumerate(jewels):
            counter+=stones.count(el)
        return counter