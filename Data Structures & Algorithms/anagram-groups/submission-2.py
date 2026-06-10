class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for each_word in strs:
            
            temp = [0] * 26

            for each_char in each_word:
                temp[ord(each_char) - ord('a')] += 1
            if tuple(temp) in d:
                d[tuple(temp)].append(each_word)
            else:
                d[tuple(temp)] = [each_word]
        
        return list(d.values())