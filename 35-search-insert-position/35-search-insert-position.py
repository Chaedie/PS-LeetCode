class Solution:
    def binarySearch(nums, target, lt, rt):
        mid = (lt + rt) // 2
        
        if lt >= rt:
            if nums[lt] < target:
                return lt+1
            if nums[lt] > target:
                return lt      
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return Solution.binarySearch(nums, target, mid + 1, rt)
        if nums[mid] > target:
            return Solution.binarySearch(nums, target, lt, mid - 1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums) - 1
        return Solution.binarySearch(nums, target, lt, rt)
        