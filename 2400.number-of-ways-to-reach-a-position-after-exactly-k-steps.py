#
# @lc app=leetcode id=2400 lang=python3
#
# [2400] Number of Ways to Reach a Position After Exactly k Steps
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        alloted = 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1  # mark as used
                    alloted += 1
                    break
        return n - alloted
  
# @lc code=end

