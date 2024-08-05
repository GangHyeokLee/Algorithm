from collections import defaultdict

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

sushiType = defaultdict(int)
sushiType[c] += 1

sushi += sushi[:k-1]

for i in range(k):
  sushiType[sushi[i]] += 1
  

left = 0
right = k

ans = len(sushiType)
tmp = ans

while right < len(sushi):
  
  if sushiType[sushi[right]] == 0:
    tmp += 1
    
  sushiType[sushi[right]] += 1
  sushiType[sushi[left]] -= 1
  if sushiType[sushi[left]] == 0:
    tmp -= 1
    
  right += 1
  left += 1
    
  ans = max(ans, tmp)
  
print(ans)