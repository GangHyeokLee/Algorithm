def solution(word: str):
  mo = [ 'A', 'E', 'I', 'O', 'U']
  order = [[1, 782, 1563, 2344, 3125], [1, 157, 313, 469, 625], [1, 32, 63, 94, 125], [1, 7, 13, 19, 25], [1, 2, 3, 4, 5]]
  
  ans = 0
  for idx, w in enumerate(word):
    ans += order[idx][mo.index(w)]
  
  return ans