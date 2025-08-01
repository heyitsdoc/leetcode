#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        # Create a set to store all folder paths for fast lookup
        folder_set = set(folder)
        result = []

        
        for f in folder:
            is_sub_folder = False
            prefix = f

            
            while not prefix == "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break

            
                prefix = prefix[0:pos]
                
                if prefix in folder_set:
                    is_sub_folder = True
                    break

            if not is_sub_folder:
                result.append(f)
        return result
# @lc code=end

