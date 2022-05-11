class Solution:
    def reverseWords(self, s: str) -> str:
        # 2nd sol
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

        result =""
        for char in tmp:
            result += char
        return result

                
        ## 뒤에서부터 leftIndex -=1 하면서  0찾아 내려오기
        ## 0 찾으면 leftIndex + 1 부터, rightIndex 까지 스위칭하기
        ## rightIndex = leftIndex - 1
        ## leftIndex - 1 부터 leftIndex -= 1 하면서  0찾아 내려오기 반복
        ## leftindex == -1 되면 종료
        
        ## result =""
        ## for char in tmp:
        ##      result += char
        
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

       
        
        
            