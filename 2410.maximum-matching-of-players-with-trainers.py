#
# @lc app=leetcode id=2410 lang=python3
#
# [2410] Maximum Matching of Players With Trainers
#

# @lc code=start
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i , j = 0 ,0
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i +=1
                j +=1
                count += 1
            else:
                j +=1
        return count 
# @lc code=end

