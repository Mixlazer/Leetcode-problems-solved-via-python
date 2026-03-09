class Solution:
    def minOperations(self, s: str) -> int:
        counter1, counter2=0, 0
        for i, el in enumerate(s):
            if not ((i%2==0 and el=="1") or (i%2==1 and el=="0")):
                counter1+=1
            elif not ((i%2==1 and el=="1") or (i%2==0 and el=="0")):
                counter2+=1
        return min(counter1, counter2)