import sys
sys.setrecursionlimit(10 ** 6)

def solution(numbers):
    answer = []    
    
    for n in numbers:
        b = list(map(int, list(str(bin(n))[2:])))
        if maketree(b):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

def maketree(n):
    l = 0
    while 2**(l+1)-1 < len(n):
        l += 1
    tree = [0] * (2 ** (l + 1) - 1 - len(n)) + n
    
    return dfs(tree, len(tree)//2)
    
def dfs(tree, now):
    if sum(tree) == 0:
        return True
    elif tree[now] == 0:
        return False
    elif len(tree) == 3:
        return True
    
    ltree = tree[:now]
    rtree = tree[now+1:]
    
    return dfs(ltree, len(ltree)//2) and dfs(rtree, len(rtree)//2)
    