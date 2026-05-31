class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dic = {c : set() for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    dic[w1[j]].add(w2[j])
                    break
        print(dic)
        visited = {}
        res =[]
        
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            
            for n in dic[c]:
                if dfs(n):
                    return True
            
            visited[c] = False
            res.append(c)
            return False

        for c in dic:
            if dfs(c):
                return ""
        print(res)
        res.reverse()
        return "".join(res)