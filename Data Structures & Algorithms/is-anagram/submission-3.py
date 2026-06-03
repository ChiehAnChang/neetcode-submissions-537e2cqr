class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ch_dic = [0] * 26

        for each_c in s:
            ch_dic[ord(each_c) - ord('a')] += 1

        for each_t in t:
            index = ord(each_t) - ord('a')
            if ch_dic[index] > 0:
                ch_dic[index] -= 1
            else:
                return False

        return True