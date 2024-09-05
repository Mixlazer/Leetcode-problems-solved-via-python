class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Инициализация стека с -1 для обработки случаев валидной строки с начала

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Добавляем индекс открывающей скобки в стек
            else:
                stack.pop()  # Убираем индекс предыдущей открывающей скобки

                if not stack:
                    stack.append(i)  # Если стек пуст, добавляем текущий индекс
                else:
                    max_len = max(max_len, i - stack[-1])  # Вычисляем длину валидной подстроки

        return max_len

print(Solution().longestValidParentheses(")()())"))




