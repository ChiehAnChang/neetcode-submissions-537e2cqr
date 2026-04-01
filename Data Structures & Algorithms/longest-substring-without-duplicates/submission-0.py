class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = 0
        right = 0
        curr_max = 0

        while right < len(s):
            ch = s[right]
            # 修改點 1: 判斷重複時，要確保這個重複是在 left 之後 (有效窗口內)
            if ch in d and d[ch] >= left:
                # 修改點 2: 直接跳到該重複字元的下一格
                left = d[ch] + 1
            
            # 修改點 3: 無論是否重複，都要更新位置和計算長度
            d[ch] = right
            curr_max = max(right - left + 1, curr_max)
            
            right += 1
        
        return curr_max