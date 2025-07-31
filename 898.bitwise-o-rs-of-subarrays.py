#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#

# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current =  set()

        for n in arr:
            nextOr = {n | y for y in current}
            nextOr.add(n)
            result.update(nextOr)
            current = nextOr
        
        return len(result)
# @lc code=end

