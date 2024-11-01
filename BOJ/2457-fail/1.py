n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
flowers.sort()

cnt = 1
cm, cd = 3, 1
em, ed = 0, 0

for f in flowers:
    
    if em == 12:
        break

    m, d, fm, fd = f

    if m > cm or (m == cm and d > cd):
        cm, cd = em, ed
        cnt += 1
    
    if (m < cm) or (m == cm and d <= cd):
        if em < fm:
            em, ed = fm, fd
        elif em == fm:
            ed = max(fd, ed)
    else:  
        cnt = 0
        break
    
print(cnt if em == 12 else 0)