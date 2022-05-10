class Solution:
    def reverseWords(self, s: str) -> str:
        
        def switchWordOder(start):
            end = start + 1

            for i in range(n):
                if end >= n:
                    end = end - 1
                    break
                if s[end] == " ":
                    end = end - 1
                    break
                end += 1

            for i in range(0, end - start + 1):
                tmp[start + i], tmp[end - i] = s[end - i], s[start + i]

            return end + 2

        start = 0
        n = len(s)
        tmp = [" " for _ in range(n)]

        while start < n:
            start = switchWordOder(start)

        result = ""
        for char in tmp:
            result += char
        return result

        
            