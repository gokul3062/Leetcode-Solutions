'''
Question:

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".


Solution:
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        # HashMap to store the count of characters 'a', 'b', and 'c'
        c = defaultdict(int)
        res = l = 0  # 'l' is the left pointer

        for r in range(N):
            c[s[r]] += 1  # Include the current character in the window

            while c['a'] > 0 and c['b'] > 0 and c['c'] > 0:
                c[s[l]] -= 1  # Remove the leftmost character
                # Example: "abc abc"
                #               --- 
                # When r = 2 ("abc" found), all substrings starting at 'l' and ending at
                # any index >= r are valid. So we add (N - r) to 'res'.
                res += N - r  
                l += 1  # Move the left pointer to check for the next valid window

        return res
