# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lt = 1
        rt = n
        def binarySearch(lt, rt):
            mid = (lt + rt) // 2
            mid_center = isBadVersion(mid) 
            mid_left = isBadVersion(mid - 1)
            mid_right = isBadVersion(mid + 1)
            
            if mid_left == False and mid_center == True:
                return mid
            if mid_center == False and mid_right == True:
                return mid + 1
            
            if mid_left == True and mid_center == True:
                return binarySearch(lt, mid - 1)
            
            if mid_center == False and mid_right == False:
                return binarySearch(mid + 1, rt)
            
        return binarySearch(lt, rt)
            
                
        
        