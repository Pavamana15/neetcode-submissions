class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Valid = 1

        for i in range(9):
            hashset = set()
            for val in board[i][:]:
                if val.isdigit():
                    if val in hashset:
                        Valid = 0
                        return False
                    else:
                        hashset.add(val)
        
        for i in range(9):
            hashset = set()
            for j in range(9):
                val = board[j][i]
                if val.isdigit():
                    if val in hashset:
                        Valid = 0
                        return False
                    else:
                        hashset.add(val)

        
        for box_row in range(3):
            for box_col in range(3):
                hashset = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row * 3 + i][box_col * 3 + j]
                        if val.isdigit():
                            if val in hashset:
                                return False
                            hashset.add(val)
    
        return True
        
        



        