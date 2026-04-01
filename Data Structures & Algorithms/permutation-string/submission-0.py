class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # 如果 s1 比 s2 長，不可能包含 s1 的排列，直接 false
        if n1 > n2:
            return False
        
        # 建立兩個計數陣列，對應 a-z (index 0-25)
        count1 = [0] * 26
        count2 = [0] * 26
        
        # 1. 初始化第一個視窗 (長度為 n1)
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # 檢查初始視窗是否吻合
        if count1 == count2:
            return True
        
        # 2. 開始滑動視窗 (從 index n1 開始往右滑)
        for i in range(n1, n2):
            # 加入新的字元 (右邊進來 s2[i])
            count2[ord(s2[i]) - ord('a')] += 1
            
            # 移除舊的字元 (左邊出去 s2[i - n1])
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            
            # 檢查是否吻合
            if count1 == count2:
                return True
                
        return False