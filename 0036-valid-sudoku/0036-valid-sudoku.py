class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets for rows, columns, and boxes to track digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Loop through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                # Check for duplicate in current row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check for duplicate in current col
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Calculate box index
                # Check for duplicate in current box
                box_index = (r // 3) * 3 + c // 3
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
                
        return True