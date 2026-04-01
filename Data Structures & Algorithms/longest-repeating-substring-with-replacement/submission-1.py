class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        storage = [0] * 26
        max_freq = 0
        left_i = 0
        max_len = 0

        for right_i in range(len(s)):
            ch = s[right_i]
            storage[ord(ch) - ord('A')] += 1
            # 這裡只做貪心更新沒問題，因為下面 while 會重新檢查
            max_freq = max(max_freq, storage[ord(ch) - ord('A')])

            # 【Fix 2】計算正確的窗口長度 (+1)
            curr_size_window = right_i - left_i + 1
            
            # 檢查是否合法
            while curr_size_window - max_freq > k:
                left_most_ch = s[left_i]
                storage[ord(left_most_ch) - ord('A')] -= 1
                left_i += 1
                
                # 【Fix 1】List 直接取 max，不需要 .values()
                # 注意：這行會讓複雜度變成 O(26*N)，但對於此題限制是可接受的
                max_freq = max(storage)
                
                # 更新縮小後的窗口長度以便下一輪判斷
                curr_size_window = right_i - left_i + 1

            max_len = max((right_i - left_i) + 1, max_len)

        return max_len