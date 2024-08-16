from collections import defaultdict
import datetime

def solution(today, terms, privacies):
    answer = []
    
    term = defaultdict(int)
    
    y, m, d = map(int, today.split("."))
    
    today = datetime.date(y, m, d)
    
    for t in terms:
      c, m = t.split()
      term[c] = int(m) * 28
    
    for idx, p in enumerate(privacies):
      date, c = p.split()
      y, m, d = map(int, date.split("."))
      
      d += term[c] - 1
      m += d // 28
      d %= 28
      
      if d == 0:
        m -= 1
        d += 28
      
      y += m // 12
      m %= 12
      
      if m == 0:
        y -= 1
        m += 12

      date = datetime.date(y, m, d)
      
      if today > date:
        answer.append(idx + 1)

    return answer
  
solution("2022.05.19", ["A 6", "B 12", "C 3"]	, 	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])