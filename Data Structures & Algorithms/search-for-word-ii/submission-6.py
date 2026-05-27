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
        
        res = set()
        seen = set()
        ROWS, COLS = len(board), len(board[0])
    
        def dfs(r, c, node, word):
            if ((r,c) in seen 
            or r < 0 or r > ROWS-1 
            or c < 0 or c > COLS-1 
            or board[r][c] not in node.children):
                return

            seen.add((r,c))
            node = node.children[board[r][c]]
            word+= board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            seen.remove((r,c))
            return
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        return list(res)
        