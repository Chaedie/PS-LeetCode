class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start = 0
        end = n - 1
        for _ in range(n // 2):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1