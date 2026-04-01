class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.board = board
        self.n_rows = len(board)
        self.n_cols = len(board[0])
        
        # 1. 核心遞迴函數
        # (r, c) : 我們「當前」所在的格子
        # k :      我們正在匹配 word[k]
        # path (visited) : 
        #    一個 set，包含 (r, c) 以及「之前」所有走過的格子
        #    (這完全對應 partition 模板中的 path)
        def dfs(r, c, k, path):
            
            # 3. 結束條件
            # (注意：在這個模板中，結束條件
            #  是在「上一層」的 for 迴圈中檢查的)
            # 
            # 這裡我們加一個「成功」的結束條件：
            if k == len(word) - 1:
                # 由於我們能呼叫 dfs(r, c, k)，
                # 就代表 board[r][c] == word[k] 已經被檢查過了
                # 所以 k 到了結尾，就代表成功了
                return True

            # 4. 遍歷「當前」的所有選擇
            #    「選擇」就是「上、下、左、右」四個方向
            choice_list = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            
            found = False
            for new_r, new_c in choice_list:
                
                # 我們的「選擇」是 (new_r, new_c)
                choice = (new_r, new_c)
                
                # 5. (可選) 剪枝 (Pruning)
                #    如果這個「選擇」(下一步) 不合法...
                
                # 剪枝 1: 選擇是否越界？
                if not (0 <= new_r < self.n_rows and 0 <= new_c < self.n_cols):
                    continue
                
                # 剪枝 2: 選擇是否已經在「路徑」上？
                if choice in path:
                    continue
                    
                # 剪枝 3: 選擇的格子是否匹配我們要的下一個字元 (word[k+1])？
                if self.board[new_r][new_c] != word[k + 1]:
                    continue
                
                # ----- 如果剪枝通過 (選擇合法) -----

                # 6. 做出選擇 (Make a choice)
                #    (完全對應 partition 的 path.append)
                path.add(choice)

                # 7. 進入下一層決策 (Recurse)
                #    (完全對應 partition 的 dfs(i + 1))
                if dfs(new_r, new_c, k + 1, path):
                    found = True
                    break # 找到了，立刻停止這個 for 迴圈
                
                # 8. 撤銷選擇 (Undo the choice - THE "BACKTRACK")
                #    (完全對應 partition 的 path.pop)
                path.remove(choice)

            return found

        # 9. 啟動
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.board[i][j] == word[0]:
                    
                    # 啟動時的「初始路徑」
                    initial_path = set()
                    initial_path.add((i, j)) # 做出「啟動」的選擇
                    
                    if dfs(i, j, 0, initial_path): 
                        return True
                        
        return False