class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = dict()
        for el in arr:
            bit_count = bin(el).count("1") 
            if bit_count in d: 
                d[bit_count].append(el)
            else:
                d[bit_count] = [el]
        
        single_list = []
        for bit_count in sorted(d.keys()):
            for x in sorted(d[bit_count]):
                single_list.append(x)
        return single_list