class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)
        l = len(n)

        for i in range(l-1):
            if n[i] > n[i+1]:
                break
        else:
            return int(n)


        while i>0 and n[i-1] == n[i]: i -= 1

        print(i)

        return int(str(int(n[:i+1])-1) + '9' *(l-i-1))