from collections import deque

for _ in range(int(input())):
  p = input()
  n = int(input())
  try:
    arr = deque(input().replace('[', '').replace(']', '').split(','))
    dir = True #왼쪽에서 빼기
    for o in p:
      if o == 'R':
        dir = not dir
      elif o == 'D' and dir:
        # que안에 ['']일 경우 에러로 판별 못해서 강제로 두 번 뽑기
        if(arr.popleft()==""):
          arr.popleft()
      else:
        if(arr.pop() == ""):
          arr.pop()
  except:
    print('error')
    continue     
  if not dir: #방향 바뀜
    arr.reverse()
  ans = ",".join(map(str, arr))
  print('[' + ans + ']')