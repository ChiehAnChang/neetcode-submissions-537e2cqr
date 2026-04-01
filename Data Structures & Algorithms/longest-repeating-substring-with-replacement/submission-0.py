class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}  
        left = 0
        right = 0
        curr_max = 0
        max_f = 0      

        while right < len(s):
            ch = s[right]
            
            count_map[ch] = count_map.get(ch, 0) + 1
            max_f = max(max_f, count_map[ch])
            
            while (right - left + 1) - max_f > k:
                count_map[s[left]] -= 1
                left += 1
            
            curr_max = max(right - left + 1, curr_max)
            
            right += 1
        
        return curr_max