#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res += c
        return res


# @lc code=end

