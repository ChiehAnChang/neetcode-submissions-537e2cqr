class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words_dic = defaultdict(list)
        for each_string in strs:

            
            checklist = [0] * 26
            for each_ch in each_string:
                checklist[ord(each_ch) - ord('a')] += 1
            

            words_dic[tuple(checklist)].append(each_string)

        
        result = []

        for each_ana in words_dic:
            result.append(words_dic[each_ana])
        return result