class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#         result = []
#         for num in nums:
#             result.append(num * num)
#         return sorted(result)
        
        length = len(nums)
        start = 0
        end = length - 1
        
        result = [0] * length
        for i in range(length - 1 ,-1, -1 ):
            sqr_start = nums[start] ** 2
            sqr_end = nums[end] ** 2
            
            # if start == end:
            #     result[i] = sqr_start
            #     break                                  
            if sqr_start >= sqr_end :
                result[i] = sqr_start
                start += 1
                continue
            if sqr_start <= sqr_end :
                result[i] = sqr_end
                end -= 1
                continue
        return result
            