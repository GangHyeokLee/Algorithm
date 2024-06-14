def solution(number, k):
    answer = 0
    
    def dfs(start, log, answer):
        if len(log) == len(number) - k:
            return max(int(log), answer)
        for i in range(start + 1, len(number)):
            answer = max(answer, dfs(i, log + number[i], answer))
        
        return answer
            
    for i in range(len(number)):
        answer = max(answer, dfs(i, number[i], answer))
    
    return str(answer)