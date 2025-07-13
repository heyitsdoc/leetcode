#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [num for num in nums if num != val]
        count = len(result)
        nums[:count] = result
        return count
# @lc code=end

