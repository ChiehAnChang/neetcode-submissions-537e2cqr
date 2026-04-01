class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for each_str in strs:

            a = [0] * 26
            for each_c in each_str:
                a[ord(each_c) - ord('a')] += 1
            
            d[tuple(a)].append(each_str)
        
        
        return [d[each_k] for each_k in d]
