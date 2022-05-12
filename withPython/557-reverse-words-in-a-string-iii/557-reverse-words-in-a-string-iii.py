class Solution:
    def reverseWords(self, s: str) -> str:
        # 2nd sol
        n = len(s)
        right = n - 1
        tmp = [" " for _ in range(n)]

        for left in range(n-1, -1, -1):
            if s[left] == " ":
                for j in range(right-left):
                    tmp[left + j + 1] = s[right - j]
                right = left - 1
                continue
            if left == 0:
                for j in range(right + 1):
                        tmp[left + j] = s[right - j]
        
        result = ''.join(tmp)
        return result

        # result =""
        # for char in tmp:
        #     result += char
        # return result
        
        # 1st sol
#         def switchWordOder(start):
#             end = start + 1

#             for i in range(n):
#                 if end >= n:
#                     end = end - 1
#                     break
#                 if s[end] == " ":
#                     end = end - 1
#                     break
#                 end += 1

#             for i in range(0, end - start + 1):
#                 tmp[start + i], tmp[end - i] = s[end - i], s[start + i]

#             return end + 2

#         start = 0
#         n = len(s)
#         tmp = [" " for _ in range(n)]

#         while start < n:
#             start = switchWordOder(start)

#         result = ""
#         for char in tmp:
#             result += char
#         return result
