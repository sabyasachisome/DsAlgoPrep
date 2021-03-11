"""
Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string
without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

Example 1:

Input: s = "ababa"
Output: 1
Explanation: String is already palindrome
Example 2:

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "".
Remove palindromic subsequence "a" then "bb".

Constraints:

0 <= s.length <= 1000
s only consists of letters 'a' and 'b'
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s=='':
            return 0
        if self.is_palindrome(s):
            return 1
        return 2

    def is_palindrome(self, s: str)-> int:
        start= 0
        end= len(s)-1
        while(start<end):
            if s[start]!=s[end]:
                return 0
            start+=1
            end-=1
        return 1

s = "ababab"
sol= Solution()
print(sol.removePalindromeSub(s))