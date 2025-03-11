'''
Question:

Group Anagrams

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]

Output: [["x"]]

Solution:
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        Sorting and Hashing
        key = defaultdict(list)

        for word in strs:
            w = tuple(sorted(word))
            key[w].append(word)
        
        return key.values()
        '''

        res = defaultdict(list)

        for word in strs:
            ch = [0] * 26
            for c in word:
                ch[ord(c) - ord('a')] += 1
            
            res[tuple(ch)].append(word)
        
        return res.values()
