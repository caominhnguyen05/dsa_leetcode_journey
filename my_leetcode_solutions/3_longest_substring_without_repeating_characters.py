class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0

        sett = set()
        n = len(s)

        # O(n)
        for right in range(n):
            # While window is invalid
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            
            # We have a valid window
            w = (right - left) + 1
            longest = max(longest, w)
            sett.add(s[right])

        return longest