from collections import deque, defaultdict


# https://leetcode.com/problems/word-ladder/description/

# class Solution():
#     def ladderLength(self, beginWord, endWord, wordList):
#         return None

# class Solution():
#     def ladderLength(self, beginWord, endWord, wordList):
#         if len(wordList) == 0:
#             return 0
#         if len(beginWord) != len(endWord) or len(endWord) != len(wordList[0]):
#             return 0
#         if endWord not in wordList:
#             return 0
#         return None

class Solution():
    def ladderLength(self, beginWord, endWord, wordList):
        if len(wordList) == 0:
            return 0
        if len(beginWord) != len(endWord) or len(endWord) != len(wordList[0]):
            return 0
        if endWord not in wordList:
            return 0
        wordList = list(set(wordList))

        # generate adjacency information
        adj = []
        for i in range(len(beginWord)):
            adji = defaultdict(list)
            for w in wordList:
                adji[w[:i] + w[i + 1:]].append(w)
            adj.append(adji)

        # perform BFS to find shortest path length
        q = deque()
        q.append((2, beginWord))
        visited = set([beginWord])
        while q:
            d, cur = q.popleft()
            for i in range(len(beginWord)):
                for nex in adj[i][cur[:i] + cur[i + 1:]]:
                    if nex == endWord:
                        return d
                    if nex not in visited:
                        visited.add(nex)
                        q.append((d + 1, nex))
        return 0