class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # I want to use the cycle detection theorem
        # I will use the dfs version of the cycle detection theorem

        W = 0
        G = 1
        B = 2

        status = [W for i in range(n)]
        
        # ✅ 修正錯誤：建立鄰接圖
        adj_graph = dict((i, []) for i in range(n))
        
        for each_e in edges:
            adj_graph[each_e[0]].append(each_e[1])
            adj_graph[each_e[1]].append(each_e[0])

        def dfs(node, parent):
            if status[node] == G:
                return False  # ❗ 遇到灰色表示成環
            if status[node] == B:
                return True

            status[node] = G
            for each_e in adj_graph[node]:  # ✅ 修正遍歷錯誤
                if each_e == parent:
                    continue  # ❗ 避免走回頭路（因為是無向圖）
                if not dfs(each_e, node):
                    return False
            status[node] = B
            return True

        # ✅ 從 0 開始做 DFS
        if not dfs(0, -1):
            return False

        # ✅ 確保所有節點都走訪過（圖為連通）
        return all(s == B for s in status)
