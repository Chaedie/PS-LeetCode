class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
               
        # 1st Sol:
#         n = len(nums)
#         for _ in range(k):
#             nums.insert(0, nums[n-1])
#         for _ in range(k):
#             nums.pop()
            
        # 2nd Sol:
        n = len(nums)
        k = k % n
        right = n - k
        left = 0
        tmp = nums.copy()
        for i in range(n):
            if right <= n - 1:
                nums[i] = tmp[right] 
                right += 1
            else:
                nums[i] = tmp[left]
                left += 1
        
        