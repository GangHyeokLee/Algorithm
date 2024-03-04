a, b, v = map(int, input().split())

ans = 0

ans = (v - a) // (a-b)
if (v-a) % (a-b) : ans +=1
print(ans + 1)