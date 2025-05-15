'''
Question:

You are given a string s consisting of lowercase English letters, and an integer k.
Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters in the resulting string is at most k.
Return the minimum number of deletions required to achieve this.

Example 1:
Input: s = "abc", k = 2
Output: 1
Explanation:
s has three distinct characters: 'a', 'b' and 'c', each with a frequency of 1.
Since we can have at most k = 2 distinct characters, remove all occurrences of any one character from the string.
For example, removing all occurrences of 'c' results in at most k distinct characters. Thus, the answer is 1.

Example 2:
Input: s = "aabb", k = 2
Output: 0
Explanation:
s has two distinct characters ('a' and 'b') with frequencies of 2 and 2, respectively.
Since we can have at most k = 2 distinct characters, no deletions are required. Thus, the answer is 0.

Solution:
'''

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = [0] * 26

        for c in s:
            count[ord(c) - 97] += 1
        
        count.sort(reverse=True)

        res = 0

        for i in range(26):
            if i + 1 > k:
                res += count[i]
            
        return res
