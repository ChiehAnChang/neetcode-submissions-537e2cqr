class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checklist = set()
        left = 0
        res = 0
        
        for right in range(len(s)):
            ch = s[right]
            
            while ch in checklist:
                checklist.remove(s[left])
                left += 1
            

            checklist.add(ch)
            
            res = max(res, right - left + 1)
            
        return res