def solution(numbers):
    answer = [-1] * len(numbers)
    
    max = []
    
    for i in range(len(numbers)-1, -1, -1):
        if len(max) == 0:
            max.append(numbers[i])
        elif max[-1] > numbers[i]:
            answer[i] = max[-1]
            max.append(numbers[i]) 
        elif max[-1] <= numbers[i]:
            while max and max[-1] <= numbers[i]:
                max.pop()
            if max:
                answer[i] = max[-1]
            max.append(numbers[i])
    
    return answer