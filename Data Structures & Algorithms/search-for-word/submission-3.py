class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res =  False
        seen = set()
        def dfs(i, j, idx):
            # if (i, j, idx) in seen:
            #     return False
            if idx == len(word):
                return True
            if not i in range(len(board)) or j not in range(len(board[0])) or board[i][j] != word[idx] or (i, j) in seen:
                return False    
            seen.add((i,j))
            res = (dfs(i+1, j, idx+1) or 
            dfs(i-1, j, idx+1) or
            dfs(i, j+1, idx+1) or
            dfs(i, j-1, idx+1))
            seen.remove((i, j))
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen.add((i,j, 0))
                if(dfs(i, j, 0)):
                    res = True
                    break
        return res