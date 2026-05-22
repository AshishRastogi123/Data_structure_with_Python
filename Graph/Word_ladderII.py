"""
126. Word Ladder II

link : https://leetcode.com/problems/word-ladder-ii/description/

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from collections import deque
import string
class Solution:
    def findladder(self, beginWord, endWord, wordList):
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        queue= deque()
        queue.append([beginWord])
        result = []
        while len(queue)!=0:
            level_size= len(queue)
            chosen_words = set()

            for _ in range(level_size):
                sequence= queue.popleft()
                last_word = sequence[-1]

                if last_word == endWord:
                    result.append(sequence)
                    continue
                for i in range(len(last_word)):
                    for ch in string.ascii_lowercase:
                        if ch == last_word[i]:
                            continue
                        new_word= last_word[:i] + ch + last_word[i+1:]

                        if new_word in wordset:
                            # Make a new path by appending new_word
                            new_seq = sequence + [new_word]
                            queue.append(new_seq)
                            # Mark new_word for removal after this layer
                            chosen_words.add(new_word)

            # Remove all words that were used in this layer
            for w in chosen_words:
                wordset.remove(w)

        return result

beginWord = "hit"
endWord   = "cog"
wordList  = ["hot","dot","dog","lot","log","cog"]    
s= Solution()
a=s.findladder(beginWord, endWord, wordList)
print(a)