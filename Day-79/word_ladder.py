from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:

            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):

                for char in "abcdefghijklmnopqrstuvwxyz":

                    if char == word[i]:
                        continue

                    newWord = word[:i] + char + word[i + 1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, steps + 1))

        return 0
