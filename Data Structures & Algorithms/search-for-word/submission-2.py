# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         i,j,k = 0,0,0

#         while i != len(board):
#             j = 0
#             while j != len(board[0]):
#                 print("The present word consifdered for search is:", board[i][j])
#                 if board[i][j] == word[k]:
#                     k += 1
#                     print("The present k is: ",k)
#                     print("The present word is:", board[i][j])
#                     print("The position is:" ,i,j)

#                     if k == len(word):
#                         print("The word found in the board")
#                         print("The present word is:", board[i][j])
#                         return True
                    

#                     search_space = [[i+1,j],[i,j+1],[i-1,j]]
#                     found = 0
#                     for search in search_space:
#                         if board[search[0]][search[1]] == word[k]:
#                             k += 1
#                             found += 1
#                             print("The present k is: ",k)
#                             print("The present word is:", board[search[0]][search[1]])
#                             print("The position is:" ,search[0],search[1])
#                             if k == len(word):
#                                 print("The word found in the board !!!!!")
#                                 return True
#                             i = search[0]
                      
#                             j = search[1]+1

#                             break

#                     print("The found is:", found)   
#                     if found == 0:
#                         print("No matching found")
#                         k = 0


#                 else:
#                     j += 1
#                     k = 0


#             i += 1


#         return False

                

                             


class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, m, n):
                        return True
        
        return False
    
    def dfs(self, board: List[List[str]], word: str, index: int, i: int, j: int, m: int, n: int):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        
        board[i][j] = '#'
        
        if (self.dfs(board, word, index + 1, i - 1, j, m, n)
            or self.dfs(board, word, index + 1, i + 1, j, m, n)
            or self.dfs(board, word, index + 1, i, j - 1, m, n)
            or self.dfs(board, word, index + 1, i, j + 1, m, n)):
            return True
        
        board[i][j] = word[index]
        return False
