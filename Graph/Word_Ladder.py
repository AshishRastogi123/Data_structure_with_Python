"""
127. Word Ladder
Link : https://leetcode.com/problems/word-ladder/description/

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""
import string
from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordlists):

        """
        Time Complexity : O(n * len(new_word)* 26) + o(n)
        Space Complexity : O(2n)
        """
        word_list=set(wordlists)
        if endWord  not in word_list:
            return 0
        queue=deque()
        queue.append((beginWord, 1))
        while len(queue)!=0:
            curr_word,level=queue.popleft()
            if curr_word== endWord:
                return level
            for i in range(0, len(curr_word)):
                for ch in string.ascii_lowercase:
                    if ch==curr_word[i]:
                        continue
                    new_word=curr_word[:i] + ch + curr_word[i+1:]
                    if new_word in word_list:
                        queue.append((new_word, level+1))
                        word_list.remove(new_word)
        return 0




