class Solution:
    def robotWithString(self, s: str) -> str:
        answer = ''
        alpha = Counter(s)

        t = []
        l = 'a'

        for c in s:
            t.append(c)
            alpha[c] -= 1

            while l < 'z' and alpha[l] == 0:
                l = chr(ord(l) + 1)
            
            while t and t[-1] <= l:
                answer += t.pop()

        return answer