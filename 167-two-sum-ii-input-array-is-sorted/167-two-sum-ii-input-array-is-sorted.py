class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n - 1
        
        while True:
            twoSum = numbers[start] + numbers[end]
            if twoSum == target:
                return [start + 1, end + 1]
            if twoSum > target:
                end -= 1
            if twoSum < target:
                start += 1