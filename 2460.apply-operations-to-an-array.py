#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1): 
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        result = [num for num in nums if num != 0]
        result.extend([0] * (len(nums) - len(result)))
        
        return result
        
# @lc code=end

