#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum

        
# @lc code=end

