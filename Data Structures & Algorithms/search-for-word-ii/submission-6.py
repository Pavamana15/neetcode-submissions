# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         ROWS, COLS = len(board), len(board[0])
#         path = set()
#         output = []

#         def dfs(r, c, i,word):
#             if i == len(word):
#                 return True

#             if (r< 0 or c < 0 or
#                 r >= ROWS or c >= COLS or
#                 word[i] != board[r][c] or
#                 (r, c) in path):
#                 return False

#             path.add((r, c))
#             res = (dfs(r + 1, c, i + 1,word) or
#                    dfs(r - 1, c, i + 1,word) or
#                    dfs(r, c + 1, i + 1,word) or
#                    dfs(r, c - 1, i + 1,word))
#             path.remove((r, c))
#             return res
        
#         for word in words:
#             for r in range(ROWS):
#                 for c in range(COLS):
#                     if dfs(r, c, 0,word):
#                         print("Word is found !!!!!", word)
#                         if word not in output:
#                             output.append(word)
#                             break
                
#         return output

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)