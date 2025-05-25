class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left <= right:
            mid = left + ((right - left) // 2)
            # If left neighbor is greater, find peak on the left side
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # If right neighbor is greater, find peak on the right side
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid