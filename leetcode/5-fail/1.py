class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            odd = s[left+1:right]

            if len(odd) > len(answer):
                answer = odd

            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            even = s[left+1:right]

            if len(even) > len(answer):
                answer = even

        return answer

