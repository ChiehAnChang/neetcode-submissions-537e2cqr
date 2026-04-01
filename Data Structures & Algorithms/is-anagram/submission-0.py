class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        check_list = [0] * 26
        
        for each_char in s:
            check_list[ord(each_char) - ord('a')] += 1
        
        for each_char in t:
            index = ord(each_char) - ord('a')
            check_list[index] -= 1
            if check_list[index] < 0:
                return False
                
        return True
