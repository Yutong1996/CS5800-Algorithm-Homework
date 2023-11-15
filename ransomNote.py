'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = dict()
        for le_m in magazine:
            hashmap[le_m] = hashmap.get(le_m, 0) + 1
        for le_r in ransomNote:
            if le_r in magazine and hashmap[le_r] > 0:
                hashmap[le_r] = hashmap.get(le_r, 0) - 1
            else:
                return False
        return True