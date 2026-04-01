class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] * 26
        for each_char in s:
            array[ord(each_char.lower()) - ord('a')] += 1
        
        for each_char in t:
            array[ord(each_char.lower()) - ord('a') ] -=1

        for each_result in array:
            if each_result !=0:
                return False
        return True
