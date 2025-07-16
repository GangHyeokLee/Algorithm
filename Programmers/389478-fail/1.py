import math

def solution(n, w, num):
    answer = 0
    max_lv = math.ceil(n / w)
    lv =  math.ceil(num / w)
    
    max_x = n % w if n % w else w
    
    if max_lv % 2 == 0:
        max_x = w - max_x + 1
    
    x = num % w if num % w else w
    
    if lv % 2 == 0:
        x = w - x + 1
    
    answer = max_lv - lv
    
    if max_lv % 2 and max_x < x or max_lv % 2 == 0 and max_x > x:
        answer -= 1
    
    return answer + 1