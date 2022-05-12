class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums) - 1
        def binarySearch(lt, rt):
            mid = (lt + rt) // 2
            
            if nums[mid] == target:
                return mid
            if lt >= rt:
                return -1            
            if nums[mid] < target:
                return binarySearch(mid + 1, rt)
            if nums[mid] > target:
                return binarySearch(lt, mid - 1)
        return binarySearch(lt,rt)