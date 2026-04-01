class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []
        path = []
        def dfs(open_n, close_n):
    
            if open_n == n and close_n == n:
                res.append("".join(path))
                return

            # 在這個問題中，「選擇列表」永遠是固定的！
            choice_list = ['(', ')'] 

            for choice in choice_list:
                
                # ----- 這是「做出選擇」之前的「剪枝」 -----
                if choice == '(':
                    if open_n >= n: # 剪枝：'(' 用完了，不能選
                        continue
                
                if choice == ')':
                    if close_n >= open_n: # 剪枝：')' 不能比 '(' 多，不能選
                        continue
                # ----------------------------------------
                
                # 1. 做出選擇
                path.append(choice)

                # 2. 遞迴
                if choice == '(':
                    dfs(open_n + 1, close_n)
                elif choice == ')':
                    dfs(open_n, close_n + 1)

                # 3. 撤銷選擇
                path.pop()
                        
                    

        dfs(0, 0)

        return res