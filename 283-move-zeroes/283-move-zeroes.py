class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # no copy array
        start = 0
        end = 0
        n = len(nums)

        for i in range(n):
            if start >= n:
                break
            if nums[start] == 0:
                while True:    
                    end += 1
                    if end >= n:
                        break
                    if nums[end] != 0:
                        nums[start], nums[end] = nums[end], nums[start]
                        break
            if nums[start] != 0:
                start += 1
                end = start
                    
                
           