from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_row = len(board)
        num_col = len(board[0])

        # Check rows
        for row_i in range(num_row):
            check_set = set()

            for col_i in range(num_col):
                num = board[row_i][col_i]

                if num == ".":
                    continue

                if num in check_set:
                    return False

                check_set.add(num)

        # Check columns
        for col_i in range(num_col):
            check_set = set()

            for row_i in range(num_row):
                num = board[row_i][col_i]

                if num == ".":
                    continue

                if num in check_set:
                    return False

                check_set.add(num)

        # Check 3x3 boxes
        boxes = {}

        for row_i in range(num_row):
            for col_i in range(num_col):
                num = board[row_i][col_i]

                if num == ".":
                    continue

                box_position = (row_i // 3, col_i // 3)

                if box_position not in boxes:
                    boxes[box_position] = set()

                if num in boxes[box_position]:
                    return False

                boxes[box_position].add(num)

        return True