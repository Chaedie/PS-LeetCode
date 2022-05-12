class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # no copy array
        # my First sol
#         start = 0
#         end = 0
#         n = len(nums)

#         for i in range(n):
#             if start >= n:
#                 break
#             if nums[start] == 0:
#                 while True:    
#                     end += 1
#                     if end >= n:
#                         break
#                     if nums[end] != 0:
#                         nums[start], nums[end] = nums[end], nums[start]
#                         break
#             if nums[start] != 0:
#                 start += 1
#                 end = start
                
        # better Sol
        n = len(nums)
        indexNonZero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[indexNonZero] = nums[i]
                indexNonZero += 1
        for i in range(indexNonZero, n):
            nums[i] = 0
                
                    
                
           