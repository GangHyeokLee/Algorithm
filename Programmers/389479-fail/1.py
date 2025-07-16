import math

def solution(players, m, k):
    answer = 0
    
    servers = [0] * 24
    current = 0
    
    for i in range(24):
        need = players[i] // m
        
        if i >= k:
            current -= servers[i - k]
        
        if current < need:
            servers[i] = need - current
            current = need
        
    print(servers)
    
    return sum(servers)