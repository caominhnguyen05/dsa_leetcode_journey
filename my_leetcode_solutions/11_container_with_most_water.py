from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)

        left = 0
        right = n - 1

        while left < right:
            heightt = min(height[left], height[right])
            width = right - left
            area = width * heightt
            max_area = max(max_area, area)
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area