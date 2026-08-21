class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            row_set = set()
            col_set = set()

            for c in range(9):

                if board[r][c] != ".":
                    if board[r][c] in row_set:
                        return False
                    row_set.add(board[r][c])
                        
                if board[c][r] != ".":
                    if board[c][r] in col_set:
                        return False
                    col_set.add(board[c][r])
        
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):

                box_set = set()

                for r in range(row_box, row_box + 3):
                    for c in range(col_box, col_box + 3):

                        if board[r][c] != ".":
                            if board[r][c] in box_set:
                                return False
                            box_set.add(board[r][c])
        
        return True 
                
    


        


