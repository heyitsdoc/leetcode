#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#

# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        parity = [num % 2 for num in nums ]

        def check(s_parity,alt=False):
            count = 0
            for p in parity:
                if p == s_parity:
                    count += 1
                    if alt:
                        s_parity ^= 1
            return count
        return max(
        check(0, False),  
        check(1, False),  
        check(0, True),   
        check(1, True)    
        )
        
# @lc code=end

