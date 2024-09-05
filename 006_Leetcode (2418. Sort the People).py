class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        x={}
        dictionary = dict(zip(heights, names))
        return list(dict(sorted(dictionary.items(), reverse=True)).values())


print(Solution.sortPeople(["Alice","Bob","Bob"],[155,185,150]))