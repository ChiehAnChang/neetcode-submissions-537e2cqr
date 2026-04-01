class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        picked_i = set() # 存放已經使用過的「索引」 (index)
        
        # 我們把 path 和 picked_i 都當作遞迴過程中的「狀態」
        def dfs(path, picked_i):
            
            # 結束條件：當 path 填滿時，找到一個解
            if len(path) == len(nums):
                res.append(path.copy()) # 沒錯！用 .copy()
                return # 結束當前遞迴

            # 遍歷所有「選擇」
            # 對於排列問題，每一層都可以從 0 開始選
            for each_choice_i in range(len(nums)):
                
                # 剪枝：如果這個「索引」用過了，就跳過
                if each_choice_i in picked_i:
                    continue
                
                each_choice = nums[each_choice_i]

                # 1. 做出選擇 (Make Choice)
                # 不僅 path 要加，picked_i 也要加
                path.append(each_choice)
                picked_i.add(each_choice_i) # 修正點 1: 在呼叫 dfs 之前 add

                # 2. 進入下一層決策 (Recurse)
                dfs(path, picked_i) # 修正點 2: 直接傳遞修改後的 set

                # 3. 撤銷選擇 (Undo Choice / Backtrack)
                # 兩邊都要撤銷！
                path.pop()
                picked_i.remove(each_choice_i) # 修正點 3: 必須 remove

        # 啟動！
        dfs([], picked_i)
        return res