#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
                
        
# @lc code=end

