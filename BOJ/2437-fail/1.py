n = int(input())
sum = 0
for w in sorted(list(map(int, input().split()))):
    if sum + 1 >= w:
        sum += w
    else:
        break
print(sum+1)