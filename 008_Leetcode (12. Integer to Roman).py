class Solution:
    def intToRoman(self, num: int) -> str:
        #dictionaryrewersed={v: k for k, v in dictionary.items()}
        dictionaryrewersed={0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        preresult = []
        result = ''
        length=len(str(num))
        for i in range(len(str(num))):
            stringnum=str(num)[i]
            digit=int(stringnum)*10**(length-i-1)
            digit1=int(stringnum)
            if digit1 < 2:
                preresult.append(digit1 * dictionaryrewersed[digit])
            if 1<digit1<4:
                preresult.append(digit1*dictionaryrewersed[(digit//digit1)])
            if digit1==4 or digit1==9:
                preresult.append(dictionaryrewersed[digit])
            if 4<digit1<9:
                preresult.append(dictionaryrewersed[5*10**(length-i-1)]+(digit1-5)*dictionaryrewersed[10**(length-i-1)])
        #print(digit,digit1,result,(digit1[1]-5)*10**(len(str(num))-1-1) )
        return ''.join(preresult)

print(Solution().intToRoman(200))