class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0 - k
        end = n - k
        
        # 1st Sol:
        for _ in range(k):
            nums.insert(0, nums[n-1])
        for _ in range(k):
            nums.pop()
            
            
        # 2nd Sol:
        