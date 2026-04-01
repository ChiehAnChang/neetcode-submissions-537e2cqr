class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        storage = [0] * 26
        for each_char in s:
            
            storage[ord(each_char) - ord('a')] += 1

        for each_char in t:
            if storage[ord(each_char) - ord('a')] == 0:
                return False
            storage[ord(each_char) - ord('a')] -= 1
        return sum(storage) == 0
