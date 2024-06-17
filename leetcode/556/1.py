class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        i = len(s) - 2
        for i in range(i, -1, -1):
            if s[i] < s[i+1]:
                break
        else:
            return -1

    
        for j in range(len(s)-1, i, -1):
            if s[j] > s[i]:
                s[j], s[i] = s[i], s[j]
                break
        
        s = s[:i+1] + sorted(s[i+1:])
        answer = int(''.join(s))
        return answer if answer <= 2 ** 31 - 1 else -1