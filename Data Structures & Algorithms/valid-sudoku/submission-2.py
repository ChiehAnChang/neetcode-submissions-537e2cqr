class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for each_row in board:
            row_check = set()
            for each_col in each_row:
                if each_col != "." and each_col in row_check:
                    return False
                elif each_col != "." and each_col not in row_check:
                    row_check.add(each_col)
        num_row, num_col = len(board), len(board[0])

        for each_col_j in range(num_col):
            col_check = set()
            for each_row_i in range(num_row):
                val = board[each_row_i][each_col_j]
                if val != "." and val in col_check:
                    return False
                elif val != "." and val not in col_check:
                    col_check.add(val)

        d = defaultdict(set)

        for each_row_i in range(num_row):
            for each_col_j in range(num_col):
                # get the key 
                row = each_row_i // 3
                col = each_col_j // 3
                val = board[each_row_i][each_col_j]
                if val != "." and val in d[(row, col)]:
                    return False
                elif val != "." and val not in d[(row, col)]:
                    d[(row, col)].add(val)
        return True




        