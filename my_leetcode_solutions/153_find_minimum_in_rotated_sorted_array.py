from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the min element is on the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]