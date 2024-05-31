def dfs(hash: dict, start, answer, course: list):
  if start not in hash or not hash[start]:
    answer.append(course.copy())
    return
  
  for i in range(len(hash[start])):
    course.append(hash[start][i])
    
    nhash = hash.copy()
    nhash[start] = nhash[start][:i] + nhash[start][i+1:]
    dfs(nhash, hash[start][i], answer, course)
    course.pop()
  

def solution(tickets):
    answer = []
    
    hash = dict()
    
    for t in tickets:
      if t[0] in hash:
        hash[t[0]].append(t[1])
      else:
        hash[t[0]] = [t[1]]
    
    dfs(hash, 'ICN', answer, ['ICN'])
    
    answer.sort()
    
    for a in answer:
      if len(a) == len(tickets) + 1:
        return a
  
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])