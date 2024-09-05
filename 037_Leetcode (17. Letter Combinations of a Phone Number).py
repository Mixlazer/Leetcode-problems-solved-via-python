class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keypad_mapping = {
            '1': '○○',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '*': '*+',
            '0': '⎽⎺',
            '#': '↑#'
        }
        output=[]
        if len(digits) == 0:
            return output
        if len(digits) > 0:
            for i in keypad_mapping[digits[0]]:
                if len(digits) == 1:
                    output.append(i)
                if len(digits) > 1:
                    for j in keypad_mapping[digits[1]]:
                        if len(digits) == 2:
                            output.append(i + j)
                        if len(digits) > 2:
                            for k in keypad_mapping[digits[2]]:
                                if len(digits) == 3:
                                    output.append(i + j + k)
                                if len(digits) > 3:
                                    for l in keypad_mapping[digits[3]]:
                                        output.append(i+j+k+l)
        return output

print(Solution().letterCombinations(digits = "2"))