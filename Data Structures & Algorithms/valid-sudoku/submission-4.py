class Solution:
    def checkSquare(self, i: int, j: int, board: List[List[str]]) -> bool:
        s = set()
        count = 0
        for k in range(3):
            for l in range(3):
                if board[i + k][j + l].isalnum():
                    s.add(board[i + k][j + l])
                    count += 1
        
        if len(s) != count:
            return False

        return True

    def checkCols(self, j: int, board: List[List[str]]) -> bool:
        s = set()
        count = 0
        for k in range(9):
            if board[k][j].isalnum():
                s.add(board[k][j])
                count += 1
        
        if len(s) != count:
            return False
        
        return True

    def checkRows(self, i: int, board: List[List[str]]) -> bool:
        s = set()
        count = 0
        for k in range(9):
            if board[i][k].isalnum():
                s.add(board[i][k])
                count += 1
        
        if len(s) != count:
            return False
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                if not self.checkSquare(i*3, j*3, board):
                    return False
        
        for j in range(9):
            if not self.checkCols(j, board):
                return False
        
        for i in range(9):
            if not self.checkRows(i, board):
                return False
        
        return True
        