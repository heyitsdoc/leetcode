#
# @lc app=leetcode id=3136 lang=python3
#
# [3136] Valid Word
#

# @lc code=start
class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        if len(word) > 3:
            return False
        vowels = {'a', 'e', 'i', 'o', 'u'}
        is_vowel = False
        is_consonant = False
        for char in word:
            if not char.isalpha():
                return False
            if char in vowels:
                is_vowel = True
            else:
                is_consonant = True
        return is_vowel and is_consonant
        
            
            


# @lc code=end

