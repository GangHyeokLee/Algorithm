def solution(prices):
    answer = [0] * len(prices)
    
    for idx, itm in enumerate(prices):
      up = 0
      if idx == len(prices)-1:
        answer[idx] = 0
      else:
        for i in range(idx + 1, len(prices)):
          up+=1
          answer[idx] = up
          if itm > prices[i]:
            break
    return answer
  
print(solution([1, 2, 3, 2, 3]))