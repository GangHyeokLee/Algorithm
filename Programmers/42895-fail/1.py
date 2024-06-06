def solution(N, number):
    if N == number:
        return 1
    
    memo = [set() for _ in range(9)]
    memo[1].add(N)
    
    for i in range(2, 9):
        memo[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for x in memo[j]:
                for y in memo[i - j]:
                    memo[i].add(x + y)
                    memo[i].add(x - y)
                    memo[i].add(y - x)
                    memo[i].add(x * y)
                    if y != 0:
                        memo[i].add(x // y)
                    if x != 0:
                        memo[i].add(y // x)
        
        if number in memo[i]:
            return i
    
    return -1