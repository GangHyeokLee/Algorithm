def solution(name):
    updown = 0
    
    for c in name:
        updown+=min(ord(c) - ord('A'), abs(ord('Z') - ord(c)) + 1)
    
    min_move = len(name) - 1
    
    while name[min_move] == "A" and min_move>0:
        min_move-=1
    
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, i + i + len(name) - next, (len(name) - next) * 2 + i)
    
    return updown + min_move