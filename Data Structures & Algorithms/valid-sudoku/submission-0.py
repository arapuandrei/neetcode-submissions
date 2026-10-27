class Solution:
    def checkColumn(self,board,j):
        s = set()
        for i in range(0, 9):
            if board[i][j] in s and board[i][j]!='.':
                return False
            s.add(board[i][j])
        return True

    def checkRow(self,board,i):
        s = set()
        for j in range(0, 9):
            if board[i][j] in s and board[i][j]!='.':
                return False
            s.add(board[i][j])
        return True
    def checkNine(self,board,k):
        p = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        s= set()
        for i in range(p[k][0],p[k][0]+3):
            for j in range(p[k][1],p[k][1]+3):
                print([i,j])
                if board[i][j] in s and board[i][j]!='.':
                    print([i,j],p[i], board[i][j],s)
                    return False
                s.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = True
        for i in range(0,9):
            b = b and self.checkRow(board,i) and self.checkColumn(board,i) and self.checkNine(board,i)
            print(self.checkRow(board,i) , self.checkColumn(board,i) , self.checkNine(board,i))
        return b
