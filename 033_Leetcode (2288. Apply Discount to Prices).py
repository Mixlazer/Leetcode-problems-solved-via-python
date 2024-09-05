class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        splited = sentence.split()
        discount = 1 - discount / 100

        res = []
        for x in splited:
            n = x[1:]
            if x[0] == "$" and n.isnumeric():
                res.append("$" + "{:.2f}".format(int(n) * discount))
            else:
                res.append(x)
        return " ".join(res)
print(Solution().discountPrices("there are $1 $2 and 5$ candies in the shop",30))
