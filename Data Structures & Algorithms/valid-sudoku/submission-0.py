class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Since this question frequently attempts to verify whether an element exists or not, 
        # it is great to use an array or hashmap to do it.

        maps = dict()
        maps["rows"] = dict()
        maps["cols"] = dict()
        maps["squares"] = dict()

        # There are 9 rows in total for a 9x9 board. To be scalable for future usage, 
        # we use len(board) to determine it.
        # For each row, we create an array to act as a checklist for the map, 
        # but a more memory-efficient way would be to use a hashset.

        for each_row_i in range(len(board)):
            maps["rows"][each_row_i] = set()
        
        # Similarly, we can do the same thing for the columns.
        # [Fix 1]: Moved this OUTSIDE the row loop so it doesn't get reset every time the row changes.
        for each_col_i in range(len(board[0])):
            maps["cols"][each_col_i] = set()

        # Finally, we want to deal with the squares. The question is how to determine which 
        # square the current value belongs to.
        # [Fix 2]: We need to initialize the keys for the 3x3 grid (0,0 to 2,2).
        for r in range(3):
            for c in range(3):
                maps["squares"][(r, c)] = set()

        # Run check    
        for each_row_i in range(len(board)):
            for each_col_i in range(len(board[0])):
                curr_number = board[each_row_i][each_col_i]
                
                if curr_number == '.':
                    continue

                # [Fix 3]: Changed % to // (integer division).
                # Using % would incorrectly group rows 0, 3, and 6 together. 
                # Using // correctly groups rows 0, 1, 2 into index 0.
                sub_i, sub_j = each_row_i // 3, each_col_i // 3

                if (curr_number in maps["rows"][each_row_i]) or \
                   (curr_number in maps["cols"][each_col_i]) or \
                   (curr_number in maps["squares"][(sub_i, sub_j)]):
                    return False

                maps["rows"][each_row_i].add(curr_number)
                maps["cols"][each_col_i].add(curr_number)
                maps["squares"][(sub_i, sub_j)].add(curr_number)
                
        return True