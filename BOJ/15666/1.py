n, m = map(int, input().split())

nums = list(map(int, input().split()))

ans = []

def makeSeq(seq):
  global ans
  
  if len(seq)==m:
    seq = " ".join(str(s) for s in sorted(seq))
    if seq not in ans:
      ans.append(seq)
    return
  
  for i in nums:
    seq.append(i)
    makeSeq(seq)
    seq.pop()
makeSeq([])

tmp = []
for i in ans:
  tmp.append(list(map(int, i.split())))
  
tmp.sort()

for i in tmp:
  print(" ".join(map(str, i)))